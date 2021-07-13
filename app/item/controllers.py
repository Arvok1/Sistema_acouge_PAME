from .models import Item
from flask import request, jsonify
from flask.views import MethodView
from app.extensions import db

class ItemCreate(MethodView):#/loja/item/create 
    def get(self):
        print("oi")

    def post(self):
        print("oi")

class ItemDetails(MethodView):#/loja/item/details 
    def get(self):
        print("oi")

    def post(self):
        print("oi") 

class ItemModify(MethodView):#/loja/item/modify 
    def get(self):
        print("oi")
        
    def post(self):
        print("oi")
