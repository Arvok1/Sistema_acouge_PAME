from ..extensions import db 

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True)
    horario_atualizado = db.Column(db.Time(timezone=True))
    nome = db.Column(db.String(50))
    validade = db.Column(db.DateTime)#validade em modo data para facilitar cálculos
    imagem = db.Column(db.String(30))#seria o local da imagem no servidor
    peso = db.Column(db.Float)
    valor = db.Column(db.Float)
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))
    quantidade_disponivel = db.Column(db.Integer)
    disponivel = db.Column(db.Boolean, default = True)
    pedidos = db.relationship("Itens_pedidos", back_populates="itens")


    def json(self):
        return {
            "id":self.id,
            "horario":self.horario_atualizado,
            "nome":self.nome,
            "validade":self.validade,
            "imagem":self.imagem,
            "peso":self.peso,
            "valor":self.valor,
            "loja_id":self.loja_id
        }
#o json separado é para não mandar mais informações que o necessário -> Segurança?
    def id_e_pedido(self):
        return {
            "id":self.id,
            "pedido_id":self.pedido_id,
        }

class Itens_pedidos(db.Model):
    __tablename__ = 'itens_pedidos'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    quantidade = db.Column(db.Integer)
    peso = db.Column(db.Float)
    itens = db.relationship("Item", back_populates="pedidos")
    pedidos = db.relationship("Pedido", back_populates="itens")