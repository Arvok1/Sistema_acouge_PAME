from ..extensions import db 
from flask import jsonify
import datetime

class Pedido(db.Model):
    __tablename__ = 'pedido'#há uma tabela única para usuários, visto que possuir mais de uma tabela para "tipos de usuários" diferentes é um problema no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    data_horario = db.Column(db.DateTime, nullable = False)#último horário de atualização
    modo_entrega = db.Column(db.Integer)#0 no local, 1 entrega
    status = db.Column(db.Integer)#a ideia seria ser 0 para "no carrinho", "1" para reservado, "2" para comprado e "3" para finalizado
    metodo_pagamento = db.Column(db.Integer)#1 cartão de crédito, 2 pix
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    itens =  db.relationship("Itens_pedidos", back_populates="pedido")
    

    def json(self):
        return {
            "id":self.id,
            "datetime":self.data_horario,
            "modo_entrega":self.modo_entrega,
            "status":self.status,
            "metodo_pagamento":self.metodo_pagamento,
            "usuario":self.usuario_id,
            "itens":jsonify([item.json() for item in self.itens]),
        }
    

    