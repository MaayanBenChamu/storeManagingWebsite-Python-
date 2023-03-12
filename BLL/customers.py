from DAL.customers import Customers_DB

# _CUSTOMERS BLL_

 
class Customers_BLL:
    def __init__(self):
        self.__customers_db = Customers_DB()

    def get_all_customers(self):
        customers_db = self.__customers_db.get_all_Customers()

        return customers_db

    def get_one_customer(self, id):
        customer = self.__customers_db.get_one_customers(id)
        return customer

    def update_customer(self, id, obj):
        customer = {
            "ID": obj["ID"],
            "First_Name": obj["First_Name"],
            "Last_Name": obj["Last_Name"],
            "City": obj["City"]


        }

        stat = self.__customers_db.update_customers(id, customer)
        return stat

    def add_customer(self, obj):
        customer = {
            "ID": obj["ID"],
            "First_Name": obj["First_Name"],
            "Last_Name": obj["Last_Name"],
            "City": obj["City"]

        }

        stat = self.__customers_db.add_customers(customer)
        return stat

    def Delete_customer(self , id):
       stat = self.__customers_db.Delete_customer(id)
       return stat


# p = products_BLL()
# print(p.get_one_products(1) )
