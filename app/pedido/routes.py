from flask import Blueprint
from .controllers import PedidoCreate, PedidoDetails, PedidoView

pedido_api = Blueprint('pedido_api', __name__)

pedido_api.add_url_rule(
    '/pedido/create', view_func = PedidoCreate.as_view('pedido_create', methods=['GET', 'POST'])
)