from ..extensions import db 

class Loja(db.Model):
    __tablename__ = "loja"
    id = db.Column(db.Integer, primary_key=True)
    #usuarios_adm_perm
    #endereço
    #zona_entrega
    #pedidos