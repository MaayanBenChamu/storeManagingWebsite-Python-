from Routers.products import products
from Routers.customers import customers 
from Routers.purchases import Purchases

from flask import Flask
import json
from bson import ObjectId
from flask_cors import CORS

class JSONEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self,obj)


app = Flask(__name__)

CORS(app, supports_credentials=True)
app.json_encoder = JSONEncoder

app.register_blueprint(products, url_prefix="/products")
app.register_blueprint(customers, url_prefix="/customers")
app.register_blueprint(Purchases, url_prefix="/purchases")

app.run()  