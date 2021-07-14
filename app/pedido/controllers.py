from .models import Pedido
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db
import datetime

'''class PedidoCreate(MethodView):#/pedido/create -> cria um pedido
    def post(self):
        dados = request.json'''
        

class PedidoDetails(MethodView):#/pedido/details/<id> -> vê detalhes de um pedido especifico
    def get(self):
        print("vê detalhes de um pedido")

    def post(self):
        print("mudar pedidos") 

class PedidoView(MethodView):#/pedido -> vê todos os pedidos
    def get(self):
        print("ver pedido")

 
'''class PedidoBuy(MethodView):
    def post(self):'''

class ItemAddToCart(MethodView):#/item/addtocart/<int:usuario_id>
    #por não saber exatamente como funcionariam as requisições do front-end, optei por um post aqui, visto que não sei como poder ser feita a verificação de pedidos
    def post(self, usuario_id):
        dados = request.json
        itens = dados.get["itens"]
        data_horario = datetime.datetime.now()
        pedido_existente = Pedido.query.filter_by(usuario_id=usuario_id, status=0).first()#a ideia seria aceitar mais de um pedido ativo por vez, mas aqui, apenas um será possível
        if pedido_existente:
            #adiciona no pedido já existente
            pedido_existente.itens += itens
            pedido_existente.data_horario = data_horario 
            db.session.commit()
            return pedido_existente.json()

        else:
            #criará um novo pedido
            novo_pedido = Pedido(data_horario=data_horario, itens=itens, usuario_id=usuario_id, status=0)
            db.session.add(novo_pedido)
            db.session.commit()
            return novo_pedido.json()




