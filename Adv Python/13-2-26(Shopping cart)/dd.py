print("Logging to Flipkart")
i=0
while i<3:
        print("Your cart is empty, buy some item\n1.Add \n2.remove \n3.Exit")
        response=int(input("Tell your response : "))

        if response==1:
            print("Enter 'buy' to add item and 'stop' to stop buying items :")
            while True:
                res=input("tell your response : ")
                if(res=="buy"):
                    item=input("Enter the item :")
                    product_catalog.append(item)
    
                else:
                    print("stop buying\n")
                    break

        elif response==2:
            item=input("Enter the item to remove :")
            if item in product_catalog:
                product_catalog.remove(item)

        i=i+1