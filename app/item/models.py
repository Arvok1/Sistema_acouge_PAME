from ..extensions import db 

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True)
    horario_adicionado = db.Column(db.Time(timezone=True))
    tipo = db.Column(db.String(30))
    nome = db.Column(db.String(50))
    validade = db.Column(db.DateTime)#validade em modo data para facilitar cálculos
    imagem = db.Column(db.String(30))#seria o local da imagem no servidor
    peso = db.Column(db.Float)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    Valor = db.Column(db.Float)
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))