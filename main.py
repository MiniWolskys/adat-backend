from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from summoner.summoner import Summoner

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Summoner, '/summoner/<username>')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='localhost')
