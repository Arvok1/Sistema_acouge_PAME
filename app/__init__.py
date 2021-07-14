from flask import Flask
from .config import Config
from .extensions import db, migrate, mail
from .endereco.routes import endereco_api
from .item.routes import item_api
from .loja.routes import loja_api
from .pedido.routes import pedido_api
from .usuario.routes import user_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(endereco_api)
    app.register_blueprint(item_api)
    app.register_blueprint(loja_api)
    app.register_blueprint(pedido_api)
    app.register_blueprint(user_api)
    migrate.init_app(app, db)
    mail.init_app(app)

    return app
