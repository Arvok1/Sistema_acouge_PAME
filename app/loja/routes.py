from flask import Blueprint
from .controllers import LojaCreate

loja_api = Blueprint('loja_api', __name__)

loja_api.add_url_rule(
    '/create/loja', view_func = LojaCreate.as_view('loja_create'), methods=['GET', 'POST']
)