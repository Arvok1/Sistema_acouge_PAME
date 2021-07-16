from .usuario.models import Usuario
from .extensions import jwt

@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return usuario.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Usuario.query.filter_by(id=identity).one_or_none()


