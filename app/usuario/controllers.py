from .models import Usuario
from flask import json, request, jsonify
from flask.views import MethodView
from app.extensions import db

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
    
        if login_existente:
            return {"erro":"o login já existe"}

        if email_existente:
            return {"erro":"o email já existe"}

        else:
            novo_usuario = Usuario(nome=nome, login=login, email=email, senha=senha, telefone=telefone, endereco=endereco)

            db.session.add(novo_usuario)
            db.session.commit()

            return novo_usuario.json(), 200

class UserLogin(MethodView):#/user/login -> fazer login de usuário
    def get(self):
        print("oi")

    def post(self):
        print("oi") 

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