from ..extensions import db 

class Pedido(db.Model):
    __tablename__ = 'pedido'#há uma tabela única para usuários, visto que possuir mais de uma tabela para "tipos de usuários" diferentes é um problema no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    data_horario = db.Column(db.DateTime, nullable = False)
    modo_entrega = db.Column(db.Integer, nullable = False)
    status = db.Column(db.Integer)
    metodo_pagamento = db.Column(db.Integer)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False)
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'), nullable = False)
    itens = db.relationship("Item")
    lojas_itens = db.Column(db.Integer, db.ForeignKey('itens.loja.id'))