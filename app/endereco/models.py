from ..extensions import db 
#a escolha por uma tabela diferente deixa a organização melhor e pode facilitar numa possível integração com uma api
class Endereço(db.Model):
    __tablename__ = "endereco"
    id = db.Column(db.Integer, primary_key=True)
    #dono_endereco
    endereco = db.Column(db.String(50))
    complemento = db.Column(db.String(6))
    bairro = db.Column(db.String(10))
    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(20))
    estado = db.Column(db.String(3))
    