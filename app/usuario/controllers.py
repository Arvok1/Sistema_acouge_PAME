from .models import Usuario
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db

class UserCreate(MethodView):#/user/create -> rota para a criação de novos usuários
    def get(self):
        print("oi")

    def post(self):
        print("oi")

class UserLogin(MethodView):#/user/login -> fazer login de usuário
    def get(self):
        print("oi")

    def post(self):
        print("oi") 

class UserDetails(MethodView):#/user/details -> vê e modifica detalhes do usuário
    def get(self):
        print("oi")
        
    def post(self):
        print("oi")
