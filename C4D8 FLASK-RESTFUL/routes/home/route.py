from dataclasses import dataclass
from msilib.schema import Error
from flask_restful import Resource
from flask import request
import uuid
from matplotlib.pyplot import cla

from matplotlib.style import use

data = []

class HomeRoute(Resource):
    def get(self):
        return {'data': data}
    def post(self):
        id = str(uuid.uuid4())
        name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        user = {'id': id, 'name':name, 'last_name': last_name, 'email': email}
        data.append(user)
        return { 'data': user}

def find_user_by_id(id):

    for data_object in data:
        if data_object['id'] == id:
            return data_object
        else:
            return None

class HomeRouteWithId(Resource):
    def get(self, id):
        data_object = find_user_by_id(id)
        if(data_object):
            return {'data': data_object}
        else:
            return {'data': 'Not Found'}, 404
        
    def put(self, id):
        data_object = find_user_by_id(id)
        if(data_object):
            data_object['name'] = request.form['name']
            data_object['last_name'] = request.form['last_name']
            data_object['email'] = request.form['email']
            return {'data': data_object}
        else:
            return {'data': 'Not Found'}, 404

    def delete(self, id):
        data_object = find_user_by_id(id)
        if(data_object):
            data.remove(data_object)
            return {'data': 'DELETEED'}
        else:
            return {'data': 'Not Found'}, 404