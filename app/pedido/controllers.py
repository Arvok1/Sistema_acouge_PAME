from .models import Pedido
from ..item.models import Item, Itens_pedidos
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db
import datetime
from flask_jwt_extended import jwt_required, current_user
from ..decorators import user_lookup_callback, user_identity_lookup

'''class PedidoCreate(MethodView):#/pedido/create -> cria um pedido
    def post(self):
        dados = request.json'''
        

class PedidoDetails(MethodView):#/pedido/details/<id> -> vê detalhes de um pedido especifico
    def get(self):
        print("vê detalhes de um pedido")

    def post(self):
        print("mudar pedidos") 

class PedidoView(MethodView):#/pedido -> vê todos os pedidos
    def get(self, usuario_id):
        pedidos = Pedido.query.filter_by(usuario_id = usuario_id)
        return jsonify([pedido.json() for pedido in pedidos]), 200


 
class PedidoBuy(MethodView):
    decorators = [jwt_required]

    def get(self, pedido_id, usuario_id):
        
        if not current_user.id == usuario_id:
            return {"erro":"Usuário sem permissão"}, 400

        else:
            pedido = Pedido.query.filter_by(id=pedido_id).first()
            return pedido.json()

    def post(self, pedido_id, usuario_id):

        if not current_user.id == usuario_id:
            return {"erro":"Usuário sem permissão"}, 400
        
        else:
            dados = request.json
            
            pedido = Pedido.query.filter_by(id=pedido_id).first()
            pedido.metodo_pagamento = dados.get["metodo_pagamento"]
            pedido.modo_entrega = dados.get["modo_entrega"]
            pedido.data_horario = datetime.datetime.now()#atualiza o horário do pedido, para que a loja possa ver quando o mesmo foi comprado e se preparar, pode ser utilizado pra filtragem no futuro
            pedido.status = 2
            itens_pedidos = Itens_pedidos.query.filter_by(pedido_id = pedido_id).all()
            
            #a funçao abaixo vai iterar pela tabela itens_pedidos, com todos os itens que foram adicionados a esse pedido
            #e sempre que passar por uma linha nova, procurará o item, diretamente na tabela do mesmo e atualizará a quantidade
            # disponível, diminuindo diretamente usando o "item unico", que é a linha da relação item_pedido, após isso, 
            # verificará se a quantidade disponível é igual a 0, caso seja, colocará a disponibilidade como false, o que impede
            # que o item seja mostrado na lista mostrada ao usuário
             
            for item_unico in itens_pedidos:
                item = Item.query.filter_by(id=item_unico.item_id).first()
                item.quantidade_disponivel = item.quantidade_disponivel - item_unico.quantidade 
                if item.quantidade_disponivel == 0:
                    item.disponivel = False
                else:
                    item.disponivel = True
            
            db.session.commit()
            return pedido.json()

class ItemAddToCart(MethodView):#/item/addtocart/<int:usuario_id>
    #por não saber exatamente como funcionariam as requisições do front-end, optei por um post aqui, visto que não sei como poder ser feita a verificação de pedidos
    def post(self, usuario_id):
        dados = request.json
        itens = dados.get["itens"] #receberá o id dos itens
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




