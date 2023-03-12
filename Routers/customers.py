from flask import Blueprint, jsonify, request
from BLL.customers import Customers_BLL

customers = Blueprint('customers', __name__)

customers_bll = Customers_BLL()


# __CUSTOMERS__
# Get all:
@customers.route("/" , methods=["GET"])
def get_all_Customers():
    Customers = customers_bll.get_all_customers()
    return jsonify(Customers)

# Get one by ID;
@customers.route("/<int:id>" , methods=["GET"])
def get_one_customer(id):
    customer = customers_bll.get_one_customer(id)
    return jsonify(customer)

#Update customer:
@customers.route("/<int:id>" , methods=["PUT"]) 
def update_customer(id):
    obj = request.json
    stat = customers_bll.update_customer(id , obj)
    return jsonify(stat)

# Add one:
@customers.route("/" ,methods=["POST"] )
def Add_customer():
    obj = request.json
    stat = customers_bll.add_customer(obj)
    return jsonify(stat)

# DELETE one:
@customers.route("<int:id>" , methods=["DELETE"])
def DELETE(id):
    stat = customers_bll.Delete_customer(id)
    return jsonify(stat)


    


