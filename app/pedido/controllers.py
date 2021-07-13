from .models import Pedido
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db

class PedidoCreate(MethodView):#/pedido/create -> cria um pedido
    def get(self):
        print("oi")

    def post(self):
        print("oi")

class PedidoDetails(MethodView):#/pedido/details/<id> -> vê detalhes de um pedido especifico
    def get(self):
        print("oi")

    def post(self):
        print("oi") 

class PedidoView(MethodView):#/pedido -> vê todos os pedidos
    def get(self):
        print("oi")
        
    def post(self):
        print("oi")
 

