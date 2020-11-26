from flask import jsonify
from flask_restful import Resource

class Base(Resource):
    def renderData(self, data, schema):
      return {
        "data": schema.dump(data),
        "meta": {
          "status": 200
        }
      }
