from flask import Blueprint
from .controllers import ItemCreate, ItemDetails, ItemModify

item_api = Blueprint('item_api', __name__)

item_api.add_url_rule(
    '/loja/<int:loja_id>/item/create', view_func = ItemCreate.as_view('item_create', methods=['GET', 'POST'])
)

