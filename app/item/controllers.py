from .models import Item
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db
import datetime
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, current_user
from ..loja.models import Usuarios_lojas_permissoes
from ..decorators import user_lookup_callback, user_identity_lookup

class ItemCreate(MethodView):#/loja/<int:loja_id>/item/create
    decorators = [jwt_required]
    
    def post(self, loja_id):
        permissao_loja = Usuarios_lojas_permissoes.query.filter_by(loja_id=loja_id, usuario_id=current_user.id).first()

        if not permissao_loja.permissao > 0:
            return {"erro":"O usuário não tem permissão"}, 400 

        else:
            dados = request.json

            nome = dados.get("nome")
            
            validade = dados.get("validade")
            peso = dados.get("peso")
            valor = dados.get("valor")
            quantidade_disponivel = dados.get("quantidade_disponivel")
            horario_atualizado = datetime.datetime.now()

            novo_item = Item(nome = nome, validade=validade, peso=peso, valor=valor, loja_id=loja_id, horario_atualizado=horario_atualizado, quantidade_disponivel=quantidade_disponivel)

            db.session.add(novo_item)
            db.session.commit()

            return novo_item.json(), 200

class ItemList(MethodView):#/itens
    def get(self):
        itens = Item.query.filter_by(disponivel = True).all()
        return jsonify([item.json() for item in itens]), 200
    
        

class ItemDetails(MethodView):#/loja/item/<int:item_id>/details
    def get(self, item_id):#mostra os detalhes do item
        item = Item.query.get_or_404(item_id)
        return item.json()
    
    def patch(self, item_id):#atualiza a informações
        item = Item.query.get_or_404(item_id)
        dados = request.json

        nome = dados.get["nome", item.nome]
        horario_atualizado = datetime.datetime.now()
        validade = dados.get["validade", item.validade]
        imagem = dados.get["imagem", item.imagem]
        peso = dados.get["peso", item.peso]
        valor = dados.get["valor", item.valor]
        disponivel = dados.get["disponivel", item.disponivel]


        item.nome = nome
        item.horario_atualizado = horario_atualizado
        item.validade = validade
        item.imagem = imagem
        item.peso = peso
        item.valor = valor
        item.disponivel = disponivel

        db.session.commit()

        return item.json(), 200
        
    def delete(self, item_id):#deleta o item
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"mensagem":"item deletado da loja"}, 200








