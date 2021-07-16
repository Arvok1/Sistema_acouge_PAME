from app.sensive import Sensive as sensive

class Config:
    SQLALCHEMY_DATABASE_URI = sensive.SQLALCHEMY_DATABASE_URI #banco de dados a ser usado 
    SQLALCHEMY_TRACK_MODIFICATIONS = sensive.SQLALCHEMY_TRACK_MODIFICATIONS
    JSON_SORT_KEYS = sensive.JSON_SORT_KEYS
    MAIL_SERVER = sensive.MAIL_SERVER
    MAIL_PORT = sensive.MAIL_PORT
    MAIL_USERNAME = sensive.MAIL_USERNAME
    MAIL_KEY = sensive.MAIL_KEY
    JWT_SECRET_KEY = sensive.JWT_SECRET_KEY