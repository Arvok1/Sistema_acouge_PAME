from ..extensions import db 

class Usuario(db.Model):
    __tablename__ = 'usuario'#há uma tabela única para usuários, visto que possuir mais de uma tabela para "tipos de usuários" diferentes é um problema no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    login = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(30), unique=True)
    senha = db.Column(db.String(20))#sem "codificação"
    telefone = db.Column(db.String(10))
    endereco = db.relationship("Endereco") #criar endereco
    user_role = db.Column(db.Integer)
    pedidos = db.relationship("Pedido")
    #metodos_de_pagamento

    def json(self):
        return {
            "nome": self.nome,
            "email":self.email,
            "telefone":self.telefone
        }

    def Retornar_pedidos(self):
        return{
            "pedidos":self.pedidos
        }

    def Retornar_enderecos(self):
        return {
            "endereços":self.endereco
        }
