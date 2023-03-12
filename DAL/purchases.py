from pymongo import MongoClient

# _Purchases DAL_
class Purchases_DB:
    def __init__(self):
        self.__Client = MongoClient("localhost" , 27017)
        self.__DB = self.__Client["StoreDB"]
        self.__Purchase_Coll = self.__DB["Purchases"]

    def get_all_Purchases(self):
        Purchases = list( self.__Purchase_Coll.find({}) )
        return Purchases
        
    def get_one_Purchases(self,id):
        Purchase = self.__Purchase_Coll.find_one({"ID" : id})
        return Purchase
    
    def get_by_product_id(self , id):
        Purchases =  list(  self.__Purchase_Coll.find({"productID" : id}) )
        return Purchases

    def get_by_customer_id(self , id):
        Purchases =  list(  self.__Purchase_Coll.find({"customerID" : id}) )
        return Purchases
 
    def update_Purchase(self, id, obj):
        self.__Purchase_Coll.update_one({"ID": id}, {"$set": obj})
        return "updated"

        
    def add_Purchase(self , obj):
        self.__Purchase_Coll.insert_one(obj)
        return "Purchase has been Added!"

    def Delete_Purchase(self , id):
        self.__Purchase_Coll.delete_one({"ID":id})
        return "Purchase Deleted!"

    def Delete_purchase_by_Customer(self , id):
        self.__Purchase_Coll.delete_many({"customerID":id})
        return "Purchase Deleted!"

    def Delete_purchase_by_Product(self , id):
        self.__Purchase_Coll.delete_many({"productID":id})
        return "Purchase Deleted!"




# Purchase = Purchases_DB()
# print( Purchase.get_by_product_id(2))
