from .extensions import db 




class Usuarios_lojas_permissoes(db.Model):
    __tablename__ = 'usuarios_lojas_permissoes'
    id = db.Column(db.Integer, primary_key=True)
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    permissao = db.Column(db.Integer)#define o nivel de permissão do usuario
    usuarios = db.relationship("Usuario")