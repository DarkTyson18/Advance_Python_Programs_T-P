#Manages orders,returns, and refund.
#handle cases like invalid coupon code, out-of-stock-error, invalid payement method.

# -------- Product Inventory --------
products = {
    "Laptop": {"price": 50000, "stock": 5},
    "Phone": {"price": 20000, "stock": 10},
    "Headphones": {"price": 2000, "stock": 15}
}

valid_coupons = {"SAVE10": 0.10, "SAVE20": 0.20}

orders = {}


# -------- Custom Exceptions --------
class InvalidCouponCode(Exception):
    pass

class OutOfStockError(Exception):
    pass

class InvalidPaymentMethod(Exception):
    pass


# -------- Order Class --------
class Order:

    order_id = 1

    def place_order(self):

        product = input("Enter product name: ")

        if product not in products:
            raise OutOfStockError("Product not available")

        quantity = int(input("Enter quantity: "))

        if products[product]["stock"] < quantity:
            raise OutOfStockError("Not enough stock available")

        coupon = input("Enter coupon code (or press enter): ")

        price = products[product]["price"] * quantity

        if coupon != "":
            if coupon not in valid_coupons:
                raise InvalidCouponCode("Invalid coupon code")
            discount = price * valid_coupons[coupon]
            price -= discount

        payment = input("Enter payment method (card/upi): ")

        if payment not in ["card", "upi"]:
            raise InvalidPaymentMethod("Invalid payment method")

        products[product]["stock"] -= quantity

        order_no = "O" + str(Order.order_id)
        Order.order_id += 1

        orders[order_no] = {
            "product": product,
            "quantity": quantity,
            "amount": price
        }

        print("Order placed successfully")
        print("Order ID:", order_no)
        print("Total Amount:", price)


# -------- Return and Refund --------
class ReturnRefund:

    def return_order(self):

        order_id = input("Enter Order ID: ")

        if order_id in orders:
            product = orders[order_id]["product"]
            quantity = orders[order_id]["quantity"]

            products[product]["stock"] += quantity

            print("Return successful")
            print("Refund Amount:", orders[order_id]["amount"])

            del orders[order_id]

        else:
            print("Order not found")


# -------- Main Program --------
order_obj = Order()
return_obj = ReturnRefund()

while True:

    print("\n1. Place Order")
    print("2. Return Order")
    print("3. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == "1":
            order_obj.place_order()

        elif choice == "2":
            return_obj.return_order()

        elif choice == "3":
            break

        else:
            print("Invalid choice")

    except InvalidCouponCode as e:
        print("Error:", e)

    except OutOfStockError as e:
        print("Error:", e)

    except InvalidPaymentMethod as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)