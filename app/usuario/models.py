from ..extensions import db 

class Usuario(db.Model):
    __tablename__ = 'usuario'#há uma tabela única para usuários, visto que possuir mais de uma tabela para "tipos de usuários" diferentes é um problema no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    login = db.Column(db.String(10))
    email = db.Column(db.String(30))
    senha = db.Column(db.String(20))#sem "codificação"
    telefone = db.Column(db.String(10))
    #endereco
    user_role = db.Column(db.Integer)
    #pedidos
    #metodos_de_pagamento