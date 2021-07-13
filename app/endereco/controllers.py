from .models import Endereco
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db

class EnderecoCreate(MethodView):#/endereco/create 
    def get(self):
        print("oi")

    def post(self):
        print("oi")

