from flask import Blueprint
from .controllers import UserCreate, UserDetails

user_api = Blueprint('user_api', __name__)

user_api.add_url_rule(
    '/user/create', view_func = UserCreate.as_view('user_create', methods=['GET', 'POST'])
)

user_api.add_url_rule(
    '/user/<int:user_id>/details', view_func = UserDetails.as_view('user_details', methods=['GET', 'PATCH'])
)