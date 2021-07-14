from ..extensions import db 

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True)
    horario_adicionado = db.Column(db.Time(timezone=True))
    nome = db.Column(db.String(50))
    validade = db.Column(db.DateTime)#validade em modo data para facilitar cálculos
    imagem = db.Column(db.String(30))#seria o local da imagem no servidor
    peso = db.Column(db.Float)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    valor = db.Column(db.Float)
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))
    disponivel = db.Column(db.Boolean, default=True)

    def json(self):
        return {
            "id":self.id,
            "horario":self.horario_adicionado,
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
