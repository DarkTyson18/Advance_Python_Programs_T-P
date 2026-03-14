#Create your own custom exception for a specific application(like an inventory management system) 
#e.g- outofstockerror, invalidproductiderror, etc

inventory = {
    101: {"name": "Laptop", "price": 50000, "stock": 5},
    102: {"name": "Phone", "price": 20000, "stock": 10},
    103: {"name": "Headphones", "price": 2000, "stock": 0}
}


# Custom Exceptions
class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass


class InventorySystem:

    def purchase_product(self, product_id, quantity):

    
        if product_id not in inventory:
            raise InvalidProductIDError("Product ID does not exist")


        if inventory[product_id]["stock"] < quantity:
            raise OutOfStockError("Product is out of stock")

        inventory[product_id]["stock"] -= quantity

        print("Purchase successful!")
        print("Remaining stock:", inventory[product_id]["stock"])



system = InventorySystem()

try:
    pid = int(input("Enter Product ID: "))
    qty = int(input("Enter quantity: "))

    system.purchase_product(pid, qty)

except InvalidProductIDError as e:
    print("Error:", e)

except OutOfStockError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)