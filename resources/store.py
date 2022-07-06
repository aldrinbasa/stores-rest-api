from ast import Is
from genericpath import exists
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        else:
            return {"message": "Store with name {} does not exist.".format(name)}

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Store with name {} already exists.".format(name)}
        
        store = StoreModel(name)
        store.save_to_db()

        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
            return {"message": "{} has been deleted.".format(name)}
        else:
            return {"message": "{} does not exist.".format(name)}

class StoreList(Resource):

    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}