from flask import Blueprint
from .controllers import ItemCreate, ItemDetails, ItemList, ItemModify

item_api = Blueprint('item_api', __name__)

item_api.add_url_rule(
    '/itens', view_func = ItemList.as_view('item_list', methods=['GET'])
)
item_api.add_url_rule(
    '/loja/<int:loja_id>/item/create', view_func = ItemCreate.as_view('item_create', methods=['GET', 'POST'])
)

item_api.add_url_rule(
    '/loja/item/<int:item_id>/details', view_func = ItemDetails.as_view('item_details', methods=['GET', 'PATCH', 'DELETE'])
)
