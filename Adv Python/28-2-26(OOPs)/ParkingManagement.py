#parking lot management system
#track vehicle entry/exit, available slots, and compute parking fees

from datetime import datetime

class ParkingLot:

    def __init__(self):

        self.total_slots = 10

        self.parking_slots = {
            "P1": None, "P2": None, "P3": None, "P4": None, "P5": None,
            "P6": None, "P7": None, "P8": None, "P9": None, "P10": None
        }

        self.vehicle_entry_time = {}

        self.parking_history = {
            "Vehicle": None,
            "Slot": None,
            "Fee": None
        }

    # show available slots
    def show_details(self):

        print("\nParking Slots Status")

        cnt = 0
        for k, v in self.parking_slots.items():
            if v == None:
                cnt += 1

        print(self.parking_slots)
        print(f"Available slots : {cnt}/{self.total_slots}")


    # vehicle entry
    def vehicle_entry(self):

        vehicle_no = input("Enter Vehicle Number : ")
        slot = input("Enter parking slot (P1-P10): ")

        if self.parking_slots[slot] == None:

            self.parking_slots[slot] = vehicle_no
            self.vehicle_entry_time[vehicle_no] = datetime.now()

            self.parking_history["Vehicle"] = vehicle_no
            self.parking_history["Slot"] = slot

            print("Vehicle parked successfully")

        else:
            print("Slot already occupied")


    # vehicle exit
    def vehicle_exit(self):

        vehicle_no = input("Enter Vehicle Number : ")

        if vehicle_no in self.vehicle_entry_time:

            exit_time = datetime.now()
            entry_time = self.vehicle_entry_time[vehicle_no]

            hours = (exit_time - entry_time).seconds / 3600

            fee = max(10, int(hours * 10))

            for k, v in self.parking_slots.items():
                if v == vehicle_no:
                    self.parking_slots[k] = None

            self.parking_history["Fee"] = fee

            del self.vehicle_entry_time[vehicle_no]

            print("Vehicle Exit Successful")
            print("Parking Fee :", fee)

        else:
            print("Vehicle not found")


    # show history
    def show_history(self):

        print("\nParking Details")
        print(self.parking_history)



# create object
parking = ParkingLot()

print("\nWelcome to Smart Parking System")

while True:

    print("\n1. Check Parking Details")
    print("2. Vehicle Entry")
    print("3. Vehicle Exit")
    print("4. Show Parking History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        parking.show_details()

    elif choice == 2:
        parking.vehicle_entry()

    elif choice == 3:
        parking.vehicle_exit()

    elif choice == 4:
        parking.show_history()

    elif choice == 5:
        print("Thank you for using Parking System")
        break

    else:
        print("Invalid choice")