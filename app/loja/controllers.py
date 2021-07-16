from .models import Loja
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db
from flask_jwt_extended import jwt_required, current_user
from ..decorators import user_lookup_callback, user_identity_lookup
from ..loja.models import Usuarios_lojas_permissoes


class LojaCreate(MethodView):#/create/loja
    def get(self):
        print("pagina de criacao da loja")

    def post(self):
        print("criar uma loja")


class UsuarioLojaConfig(MethodView):
    decorators = [jwt_required]
    
    def get(self, loja_id):
        permissao_loja = Usuarios_lojas_permissoes.query.filter_by(loja_id=loja_id, usuario_id=current_user.id).first()
        
        if not permissao_loja.permissao > 0:
            return {"erro":"Você não tem permissão para ver essa página"}, 400

        else:
            permissoes_da_loja = Usuarios_lojas_permissoes.query.filter_by(loja_id=loja_id)
            return jsonify([permissao.json() for permissao in permissoes_da_loja]), 200

    def post(self, loja_id, usuario_id):
        dados = request.json
        permissao = dados.get["permissao"]

        if current_user.user_role == 0:
            return {"erro":"Usuário não tem permissão para acessar essa página"}

        else:
            nova_permissao_loja = Usuarios_lojas_permissoes(permissao = permissao, usuario_id=usuario_id, loja_id=loja_id)
            db.session.add(nova_permissao_loja)
            db.session.commit()
            
            return {"mensagem":"Usuário adicionado a loja com sucesso"}

    def patch(self, loja_id, usuario_id):
        dados = request.json

        if current_user.user_role == 0:
            return {"erro":"Usuário não tem permissão para acessar essa página"}

        else:
            permissao_loja = Usuarios_lojas_permissoes.query.filter_by(loja_id=loja_id, usuario_id=usuario_id).first()
            nova_permissao = dados.get["permissao", permissao_loja.permissao ]
            permissao_loja.permissao = nova_permissao 
            db.session.commit()

    def delete(self, loja_id, usuario_id):

        if current_user.user_role == 0:
            return {"erro":"Usuário não tem permissão para acessar essa página"}
        else:
            permissao_loja = Usuarios_lojas_permissoes.query.filter_by(loja_id=loja_id, usuario_id=usuario_id).first()
            db.session.delete(permissao_loja)
            db.session.commit()

            return {"mensagem": "A permissão de usuário foi deletada"}