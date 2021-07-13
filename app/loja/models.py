from ..extensions import db 

class Loja(db.Model):
    __tablename__ = "loja"
    id = db.Column(db.Integer, primary_key=True)
    #usuarios_adm_perm#tabela de associação com usuários e permissões que os mesmos tem, pode criar permissões como modificar loja ou uma permissão só pra criar itens e afins
    endereco = db.relationship("Endereco", back_populates="loja", uselist=False)
    zona_entrega = db.Column(db.String(100))#no estágio atual, precisa ser uma string descrevendo quais são as possíveis 
    #localidades, entretanto, com um sistema de mapa, pode ser um raio de entrega
    pedidos = db.relationship("Pedido")
    itens = db.relationship("Item")