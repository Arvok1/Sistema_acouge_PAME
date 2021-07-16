from ..extensions import db 
from flask import jsonify
from ..usuario.models import Usuario

class Loja(db.Model):
    __tablename__ = "loja"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    telefone = db.Column(db.String(11))
    usuarios_permissoes = db.relationship("Usuarios_lojas_permissoes")#tabela de associação com usuários e permissões que os mesmos tem, pode criar permissões como modificar loja ou uma permissão só pra criar itens e afins
    endereco = db.relationship("Endereco", back_populates="loja", uselist=False)
    zona_entrega = db.Column(db.String(100))#no estágio atual, precisa ser uma string descrevendo quais são as possíveis 
    #localidades, entretanto, com um sistema de mapa, pode ser um raio de entrega
    
    itens = db.relationship("Item")
    

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone":self.telefone,
            "endereco":self.endereco,
            "zona_entrega":self.zona_entrega
        }

    def json_itens(self):
        return{
            "itens":jsonify([item.json() for item in self.itens])
        }

    def json_pedidos(self):
        return {
            "itens":jsonify([pedido.json() for pedido in self.pedidos_id])
        }

class Usuarios_lojas_permissoes(db.Model):
    __tablename__ = 'usuarios_lojas_permissoes'
    id = db.Column(db.Integer, primary_key=True)
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    permissao = db.Column(db.Integer)#define o nivel de permissão do usuario
    usuarios = db.relationship("Usuario")

    def json(self):
        return {
            "usuario_id":self.usuario_id,
            "permissao":self.permissao
        }