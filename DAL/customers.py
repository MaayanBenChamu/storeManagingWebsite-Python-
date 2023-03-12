from pymongo import MongoClient
 
# _CUSTOMERS DAL_
class Customers_DB:
    def __init__(self):
        self.__Client = MongoClient("localhost" , 27017)
        self.__DB = self.__Client["StoreDB"]
        self.__Customers_Coll = self.__DB["Customers"]

    def get_all_Customers(self):
        Customers = list( self.__Customers_Coll.find({}) )
        return Customers

    def get_one_customers(self,id):
        customer = self.__Customers_Coll.find_one({"ID" : id})
        return customer

    def update_customers(self, id, obj):
        self.__Customers_Coll.update_one({"ID": id}, {"$set": obj})
        return "updated"
        
        
    def add_customers(self , obj):
        self.__Customers_Coll.insert_one(obj)
        return "Customer has been Added!"

    def Delete_customer(self , id):
        self.__Customers_Coll.delete_one({"ID":id})
        return "Customer Deleted!"



# product = products_DB()
# print( product.get_one_products(1))
