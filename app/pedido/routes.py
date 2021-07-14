from flask import Blueprint
from .controllers import ItemAddToCart, PedidoDetails, PedidoView

pedido_api = Blueprint('pedido_api', __name__)

'''pedido_api.add_url_rule(
    '/pedido/create', view_func = PedidoCreate.as_view('pedido_create', methods=['GET', 'POST'])
)'''


pedido_api.add_url_rule(
    '/item/addtocart/<int:usuario_id>', view_func = ItemAddToCart.as_view('item_add_to_cart', methods=['POST'])
)