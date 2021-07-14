from .models import Item
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db

class ItemCreate(MethodView):#/loja/item/create 
    def post(self):
        print("criar item")

class ItemList(MethodView):#/itens
    def get(self):
        itens = Item.query.filter_by(disponivel=True).all()
        return jsonify([item.json() for item in itens]), 200
    #def post(self):#ao clicar no botão "adicionar ao carrinho, mandará para uma rota em app/pedido"
        

class ItemDetails(MethodView):#/loja/item/details 
    def get(self):
        print("detalhes dos itens")


'''class ItemModify(MethodView):#/loja/item/modify 
   '''

#se usa o usuario id para checar pedidos e adicionar a certo pedido, a ser definido no pedido em si



