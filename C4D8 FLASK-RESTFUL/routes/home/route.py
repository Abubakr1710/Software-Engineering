from dataclasses import dataclass
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

class HomeRouteWithId(Resource):
        