from DAL.purchases import Purchases_DB

# _Purchases_BLL_
 

class Purchases_BLL:
    def __init__(self):
        self.__purchases_db = Purchases_DB()

    def get_all_purchases(self):
        purchases_db = self.__purchases_db.get_all_Purchases()

        return purchases_db

    def get_one_purchase(self, id):
        purchase = self.__purchases_db.get_one_Purchases(id)
        return purchase

    def get_by_product_id(self, id):
        purchases = self.__purchases_db.get_by_product_id(id)
        if(len(purchases) == 0):
            return "no result"
        else:
            return purchases
 
    def get_by_customer_id(self, id):
        purchases = self.__purchases_db.get_by_customer_id(id)
        if(len(purchases) == 0):
            return "no result"
        else:
            return purchases

    def update_purchase(self, id, obj):
        purchase = {
            "ID": obj["ID"],
            "customerID": obj["customerID"],
            "productID": obj["productID"],
            "Date": obj["Date"]

 
        }

        stat = self.__purchases_db.update_Purchase(id , purchase)
        return stat

    def add_Purchase(self, obj):
        purchase = {
            "ID": obj["ID"],
            "customerID": obj["customerID"],
            "productID": obj["productID"],
            "Date": obj["Date"]

        }

        stat = self.__purchases_db.add_Purchase(purchase)
        return stat

    def Delete_purchase(self , id):
       stat = self.__purchases_db.Delete_Purchase(id)
       return stat

    def Delete_purchase_by_Customer(self , id):
       stat = self.__purchases_db.Delete_purchase_by_Customer(id)
       return stat

    def Delete_purchase_by_Product(self , id):
       stat = self.__purchases_db.Delete_purchase_by_Product(id)
       return stat
        


    