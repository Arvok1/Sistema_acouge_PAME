from .models import Usuario
from flask import json, request, jsonify, render_template
from flask.views import MethodView
from app.extensions import db, mail, jwt
from flask_mail import Message
from ..sensive import Sensive as sensive
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

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
        #endereço
        user_role = 0

        login_existente = Usuario.query.filter_by(login=login).first()
        email_existente = Usuario.query.filter_by(email=email).first()
        #checa se existe login ou email iguais, se sim, retorna um "erro" para o front
        if (not isinstance(nome, str) or not isinstance(login, str) or not isinstance(email, str) or isinstance(senha, str) or isinstance(telefone, str)):
            return {"erro":"Alguma informação foi inserida errada"}, 400
        
        if (login_existente or email_existente):
            return {"erro":"O login ou email já existe"}, 400
            
        else:#se tiver passado as duas verificações, cria um novo objeto da classe Usuario e o coloca no banco de dados
            hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())


            novo_usuario = Usuario(nome=nome, login=login, hash_senha=hash_senha, telefone=telefone, email=email, user_role=user_role)

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


        usuario = Usuario.query.filter_by(login=login).first()

        if (not usuario or not bcrypt.checkpw(senha.encode(), usuario.hash_senha)):
            return {"erro": "login ou senha inválidos"}, 400

        else:
            acess_token = create_access_token(identity=usuario.id)
            return {"mensagem": "login feito!"}, 200

class UserDetails(MethodView):#/user/details -> vê e modifica detalhes do usuário
    decorators = [jwt_required]
    
    def get(self, user_id):
        
        if (get_jwt_identity != user_id):
            return {"erro": "Usuário não permitido"}, 400

        user = Usuario.query.get_or_404(user_id)
        return user.json(), 200

    def patch(self, user_id):

        if (get_jwt_identity != user_id):
            return {"erro": "Usuário não permitido"}, 400
        
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