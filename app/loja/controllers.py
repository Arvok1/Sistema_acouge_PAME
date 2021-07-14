from .models import Loja
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db

class LojaCreate(MethodView):#/create/loja
    def get(self):
        print("pagina de criacao da loja")

    def post(self):
        print("criar uma loja")



