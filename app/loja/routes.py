from flask import Blueprint
from .controllers import LojaCreate, UsuarioLojaConfig

loja_api = Blueprint('loja_api', __name__)

loja_api.add_url_rule(
    '/create/loja', view_func = LojaCreate.as_view('loja_create'), methods=['GET', 'POST']
)



loja_api.add_url_rule(
    '/loja/users', view_func = UsuarioLojaConfig.as_view('modify_user_loja'), methods=['GET', 'POST', 'PATCH', 'DELETE']
)