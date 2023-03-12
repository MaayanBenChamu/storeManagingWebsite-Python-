from flask import Blueprint, jsonify, request
from BLL.products import products_BLL

products = Blueprint('product', __name__)

products_bll = products_BLL()


# __PRODUCTS__

# Get all:
@products.route("/" , methods=["GET"])
def get_all_products():
    products = products_bll.get_all_product()
    return jsonify(products)

# Get one by ID;
@products.route("/<int:id>" , methods=["GET"])
def get_one_product(id):
    product = products_bll.get_one_products(id)
    return jsonify(product)

#Update product:
@products.route("/<int:id>" , methods=["PUT"]) 
def update_product(id):
    obj = request.json
    stat = products_bll.update_product(id , obj)
    return jsonify(stat)

# Add one:
@products.route("/" ,methods=["POST"] )
def Add_product():
    obj = request.json
    stat = products_bll.add_product(obj)
    return jsonify(stat)

# DELETE one:
@products.route("<int:id>" , methods=["DELETE"])
def DELETE(id):
    stat =  products_bll.Delete_product(id)
    return jsonify(stat)



