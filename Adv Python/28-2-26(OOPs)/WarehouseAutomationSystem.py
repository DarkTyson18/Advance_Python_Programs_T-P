#warehouse automation system
#track goods movement, generate inventory report and forecast demand
class Warehouse:
    def __init__(self):
        self.inventory = {}
        self.movement_log = []

    def add_goods(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

        self.movement_log.append(f"Added {quantity} of {item}")

    def remove_goods(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            self.movement_log.append(f"Removed {quantity} of {item}")
        else:
            print(f"Not enough {item} in inventory to remove.")

    def generate_inventory_report(self):
        report = "Inventory Report:\n"
        for item, quantity in self.inventory.items():
            report += f"{item}: {quantity}\n"
        return report

    def forecast_demand(self, item, historical_data):
        if historical_data:
            average_demand = sum(historical_data) / len(historical_data)
            return average_demand
        else:
            return 0
        
    def display(self):
        print("Current Inventory:")
        print(self.inventory)

        print("\nMovement Log:")
        for log in self.movement_log:
            print(log)



print("\n Warehouse automation system")
warehouse = Warehouse()
while True: 
    print("1. Enter the product details")
    print("2. Remove product from ineventory")
    print("3. Show Inventory details")
    print("4. Forecast Demand")
    print("5. Show Inventory")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        p_name=input("Eenter the Product name : ")
        p_qant=int(input("Eenter the Product Qantity : "))

        warehouse.add_goods(p_name,p_qant)
        print("Product added successfully\n")

    elif choice==2:
        p_name=input("Eenter the Product name : ")
        p_qant=int(input("Eenter the Product Qantity : "))

        warehouse.remove_goods_goods(p_name,p_qant)
          
    elif choice==3:
        warehouse.generate_inventory_report()

    elif choice==4:
        item = input("Enter item to forecast demand: ")
        historical_data = input("Enter historical demand data")
        historical_data = list(map(int, historical_data.split()))
        forecast = warehouse.forecast_demand(item, historical_data)
        print("\nForecasted Demand:",warehouse.forecast_demand())

    elif choice==5:
        warehouse.display()

    elif choice==6:
        break

    else:
        print("Wrong input")
