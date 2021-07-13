from ..extensions import db 

class Pedido(db.Model):
    __tablename__ = 'pedido'#há uma tabela única para usuários, visto que possuir mais de uma tabela para "tipos de usuários" diferentes é um problema no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    #data/horario
    #modo_entrega
    #status
    #metodo_pagamento
    #usuario
    #loja
    #Itens