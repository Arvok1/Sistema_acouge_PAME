from .models import Usuario
from flask import json, request, jsonify, render_template
from flask.views import MethodView
from app.extensions import db, mail
from flask_mail import Message
from ..sensive import Sensive as sensive

class UserCreate(MethodView):#/user/create -> rota para a criação de novos usuários
    def get(self):
        print("página que mostrará uma criação de usuário")#

    def post(self):#após a criação poderá retornar a página de itens ou algum erro
        dados = request.json

        nome = dados.get("nome")
        login = dados.get("login")
        email = dados.get("email")
        senha = dados.get("senha")
        telefone = dados.get("telefone")
        endereco = dados.get("endereco")

        login_existente = Usuario.query.filter_by(login=login) 
        email_existente = Usuario.query.filter_by(email=email)
        #checa se existe login ou email iguais, se sim, retorna um "erro" para o front
        if login_existente:
            return {"erro":"o login já existe"}

        if email_existente:
            return {"erro":"o email já existe"}
        
        else:#se tiver passado as duas verificações, cria um novo objeto da classe Usuario e o coloca no banco de dados
            novo_usuario = Usuario(nome=nome, login=login, email=email, senha=senha, telefone=telefone, endereco=endereco)

            db.session.add(novo_usuario)
            db.session.commit()

            #estruturação do email de boas-vindas
            msg = Message(
                sender = sensive.server_email,
                recipients = [novo_usuario.email],
                subject = 'Bem-vindo!',
                html = render_template('email.html', usuario=novo_usuario)
            )

            mail.send(msg)

            return novo_usuario.json(), 200

class UserLogin(MethodView):#/user/login -> fazer login de usuário
    def get(self):
        print("pagina de login")

    def post(self):
        dados = request.json

        login = dados.get["login"]
        senha = dados.get["senha"]

        usuario = Usuario.query.filter_by(login=login)
        if usuario and usuario.senha == senha:
            return usuario.json(), 200

        else:
            return {"mensagem": "usuario ou senha incorretos"}, 200

class UserDetails(MethodView):#/user/details -> vê e modifica detalhes do usuário
    def get(self, user_id):
        user = Usuario.query.get_or_404(user_id)
        return user.json(), 200

    def patch(self, user_id):
        user = Usuario.query.get_or_404(user_id)
        dados = request.json

        nome = dados.get["nome", user.nome]
        telefone = dados.get["telefone", user.telefone]
        senha = dados.get["senha", user.senha]

        user.nome = nome
        user.telefone = telefone
        user.senha = senha

        db.session.commit()

        return user.json(), 200