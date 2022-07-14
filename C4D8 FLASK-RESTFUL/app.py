from flask import Flask
from flask_restful import Api
from routes.home.route import HomeRoute


app = Flask(__name__)
api = Api(app)


api.add_resource(HomeRoute, '/')

if __name__ == '__main__':
    app.run(debug=True)