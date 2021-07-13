from flask import Blueprint
from .controllers import EnderecoCreate

endereco_api = Blueprint('endereco_api', __name__)

endereco_api.add_url_rule(
    '/endereco/create', view_func = EnderecoCreate.as_view('endereco_create', methods=['GET', 'POST'])
)