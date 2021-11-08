from flask import Flask, json, request
from flask_restful import Resource, Api, reqparse
from flask_jsonpify import jsonify, jsonpify
from flask_cors import CORS, cross_origin

import sys

sys.setrecursionlimit(10000000)
app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def home_view():
    return "<h1>201901903</h1>"

class ConsultaDatos(Resource):
    def get(self):
        try:
            f = open("./input.xml", "r")
            input = f.read()
            print(input)
            return {'salida':input }
        except:
            print('Error')
            return {'salida':'Error'}

class ResumenIva(Resource):
    def get(self):
        try:
            return {'salida':'ResumenIva :D' }
        except:
            print('Error')
            return {'salida':'Error'}

        
api.add_resource(ResumenIva, '/ResumenIva', )        
api.add_resource(ConsultaDatos, '/ConsultaDatos', )

  
