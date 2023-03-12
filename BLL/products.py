from DAL.products import products_DB


# _PRODUCTS BLL_
class products_BLL:
    def __init__(self):
        self.__products_db = products_DB()

    def get_all_product(self):
        products_db = self.__products_db.get_all_products()

        return products_db

    def get_one_products(self,id):
        product = self.__products_db.get_one_products(id)
        return product

    def update_product(self, id, obj):
        product = {
            "ID": obj["ID"],
            "Name": obj["Name"],
            "Price": obj["Price"],
            "Quantity": obj["Quantity"]

        }

        stat = self.__products_db.update_product(id, product)
        return stat
    
    
    def add_product(self, obj):
        product = {
            "ID": obj["ID"],
            "Name": obj["Name"],
            "Price": obj["Price"],
            "Quantity": obj["Quantity"]

        }

        self.__products_db.add_product(product)
        return "Product has been Added!"
    
    
    def Delete_product(self , id):
       stat = self.__products_db.Delete_product(id)
       return stat
       
# p = products_BLL()
# print(p.get_one_products(1) )