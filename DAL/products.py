from pymongo import MongoClient

# _PRODUCTS DAL_
class products_DB:
    def __init__(self):
        self.__Client = MongoClient("localhost" , 27017)
        self.__DB = self.__Client["StoreDB"]
        self.__Product_Coll = self.__DB["Products"]

    def get_all_products(self):
        products = list( self.__Product_Coll.find({}) )
        return products
        
    def get_one_products(self,id):
        product = self.__Product_Coll.find_one({"ID" : id})
        return product

    def update_product(self, id, obj):
        self.__Product_Coll.update_one({"ID": id}, {"$set": obj})
        return "updated"

        
    def add_product(self , obj):
        self.__Product_Coll.insert_one(obj)
        return "Product has been Added!"

    def Delete_product(self , id):
        self.__Product_Coll.delete_one({"ID":id})
        return "Product Deleted!"


# product = products_DB()
# print( product.get_one_products(1))
