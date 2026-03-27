print("Wlcome to vishal mega mart online shopping store\n")
Available_list = {
    "Milk": 60,
    "Bread": 40,
    "Eggs": 80,
    "Rice": 70,
    "Sugar": 45,
    "Butter": 55,
    "Apples": 150,
    "Bananas": 60,
    "Potatoes": 30,
    "Onions": 40,
    "Cooking Oil": 130,
    "Salt": 25,
    "Tea Powder": 100,
    "Coffee": 120,
    "Toothpaste": 65,
    "Soap": 35,
    "Shampoo": 180,
    "Dishwasher Liquid": 90,
    "Toilet Paper": 40,
    "Laundry Detergent": 200
}
product_catalog=[]
total_price=0
print("Available item on our site: \n")
print(Available_list)

print("\nAvailable discount on total purchase")
print("\nif amount greater than 700---Discount of 5%\nif amount greater than 1000---Discount of 10%")
while True:
    print("\nEnter \n1.Add items \n2.remove items \n3.Show bought items \n4.Ordered item \n5.Exit")
    response=int(input("Tell your response : "))
    if response==1:
        while True:
            print("Enter 'buy' to add item and 'stop' to stop buying items :")
            res=input("tell your response : ")
            if(res=="buy"):
                j=0
                while j<1:
                    item=input("Enter the item :")
                    if item in Available_list:
                        product_catalog.append(item)
                        total_price=total_price+Available_list[item]
                        print("item Added successfully\n")
                    else:
                        print("item Not available\n")
                    j=j+1
            else:
                print("stop buying\n")
                break


    elif response==2:
        item=input("Enter the item to remove :")
        if item in product_catalog:
            total_price=total_price-Available_list[item]
            product_catalog.remove(item)
            print(f"{item} removed successfully")

    elif response==3:
        print("Bought Items :",product_catalog)
        print("Total amount :",total_price)

    elif response==4:
        if(total_price>700):
            discount_amount=total_price*0.05
            print("discount amount on your purchase : ",discount_amount)
            print("You have to pay : ",total_price - discount_amount)

        if(total_price>1000):
            discount_amount=total_price*0.1
            print("discount amount on your purchase : ",discount_amount)
            print("You have to pay : ",total_price - discount_amount)
        
        else:
            print(f"No, discount on your current purchase")

    elif response==5:
        print("Thanks for choosing us")
        break