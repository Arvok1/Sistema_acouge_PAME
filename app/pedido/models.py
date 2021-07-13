from ..extensions import db 
from flask import jsonify

class Pedido(db.Model):
    __tablename__ = 'pedido'#há uma tabela única para usuários, visto que possuir mais de uma tabela para "tipos de usuários" diferentes é um problema no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    data_horario = db.Column(db.DateTime, nullable = False)
    modo_entrega = db.Column(db.Integer, nullable = False)
    status = db.Column(db.Integer)
    metodo_pagamento = db.Column(db.Integer)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    itens = db.relationship("Item")
    lojas_itens = db.Column(db.Integer, db.ForeignKey('item.loja_id'))

    def json(self):
        return {
            "id":self.id,
            "datetime":self.data_horario,
            "modo_entrega":self.modo_entrega,
            "status":self.status,
            "metodo_pagamento":self.metodo_pagamento,
            "usuario":self.usuario_id,
            "itens":jsonify([item.json() for item in self.itens]),
            "lojas_ids":jsonify([loja.json() for loja in self.lojas_itens])
        }
    
    