from flask import Blueprint, jsonify, request
from BLL.purchases import Purchases_BLL

Purchases = Blueprint('Purchases', __name__ ,  static_folder='static', template_folder='templates')

Purchases_bll = Purchases_BLL()


# __Purchases__ 
# ________________________________________________________________________GET__
# Get all:
@Purchases.route("/" , methods=["GET"])
def get_all_Purchases():
    Purchases = Purchases_bll.get_all_purchases()
    return jsonify(Purchases) 

# Get one by ID;
@Purchases.route("/<int:id>" , methods=["GET"])
def get_one_Purchase(id):
    Purchase = Purchases_bll.get_one_purchase(id)
    return jsonify(Purchase)

# Get Purchases by product ID:
@Purchases.route("/product/<int:id>" , methods=["GET"])
def get_by_product_id(id):
    Purchase = Purchases_bll.get_by_product_id(id)
    return jsonify(Purchase)

# Get Purchases by customer ID:
@Purchases.route("/customer/<int:id>" , methods=["GET"])
def get_by_customer_id(id):
    Purchase = Purchases_bll.get_by_customer_id(id)
    return jsonify(Purchase)

# ________________________________________________________________________PUT__
#Update Purchase:
@Purchases.route("/<int:id>" , methods=["PUT"]) 
def update_Purchase(id):
    obj = request.json
    stat = Purchases_bll.update_purchase(id , obj)
    return jsonify(stat)

# ________________________________________________________________________POST___
# Add one:
@Purchases.route("/" ,methods=["POST"] )
def Add_Purchase():
    obj = request.json
    stat = Purchases_bll.add_Purchase(obj)
    return jsonify(stat)

# ________________________________________________________________________DELETE__
# DELETE one:
@Purchases.route("<int:id>" , methods=["DELETE"])
def DELETE(id):
    stat = Purchases_bll.Delete_purchase(id)
    return jsonify(stat)

# DELETE Purchase by Customer ID:
@Purchases.route("/customer/<int:id>" , methods=["DELETE"])
def DELETE_by_Customer(id):
    stat = Purchases_bll.Delete_purchase_by_Customer(id)
    return jsonify(stat)

# DELETE Purchase by product ID:
@Purchases.route("/product/<int:id>" , methods=["DELETE"])
def DELETE_by_product(id):
    stat = Purchases_bll.Delete_purchase_by_Product(id)
    return jsonify(stat)


    
 

