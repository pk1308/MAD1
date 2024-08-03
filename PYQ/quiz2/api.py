from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class MyApi(Resource):
  def get(self):
      return {"greet": "Hello from GET Api!"}

  def put(self):
      return {"greet": "Hello from PUT Api!"}

api.add_resource(MyApi, '/api/get', '/api/put', '/api/post' )

app.run()