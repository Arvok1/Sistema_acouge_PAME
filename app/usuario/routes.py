from flask import Blueprint
from .controllers import UserCreate

user_api = Blueprint('user_api', __name__)

user_api.add_url_rule(
    '/user/create', view_func = UserCreate.as_view('user_create', methods=['GET', 'POST'])
)