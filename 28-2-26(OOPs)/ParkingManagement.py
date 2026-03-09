#parking lot management system
#track vehicle entry/exit, available slots, and compute parking fees

from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_no):
        self.vehicle_no = vehicle_no
        self.entry_time = datetime.now()

class ParkingLot:

    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.parked_vehicles = {}   

    
    def park_vehicle(self, vehicle_no):

        if len(self.parked_vehicles) >= self.total_slots:
            print("Parking Lot Full!")
            return

        if vehicle_no in self.parked_vehicles:
            print("Vehicle already parked!")
            return

        vehicle = Vehicle(vehicle_no)
        self.parked_vehicles[vehicle_no] = vehicle

        print("Vehicle parked successfully")
        print("Entry Time:", vehicle.entry_time)

    def exit_vehicle(self, vehicle_no):

        if vehicle_no not in self.parked_vehicles:
            print("Vehicle not found!")
            return

        vehicle = self.parked_vehicles.pop(vehicle_no)

        exit_time = datetime.now()

        duration = exit_time - vehicle.entry_time
        hours = duration.total_seconds() / 3600

        fee = self.calculate_fee(hours)

        print("Vehicle Exit Successful")
        print("Parking Time:", round(hours,2), "hours")
        print("Parking Fee: ₹", fee)

    
    def calculate_fee(self, hours):
        rate_per_hour = 20
        return max(20, int(hours * rate_per_hour))

    
    def available_slots(self):
        free = self.total_slots - len(self.parked_vehicles)
        print("Available Slots:", free)



parking = ParkingLot(5)

while True:

    print("\n----- Parking Lot Menu -----")
    print("1. Park Vehicle")
    print("2. Exit Vehicle")
    print("3. Check Available Slots")
    print("4. Exit Program")

    choice = input("Enter choice: ")

    if choice == "1":
        vehicle_no = input("Enter Vehicle Number: ")
        parking.park_vehicle(vehicle_no)

    elif choice == "2":
        vehicle_no = input("Enter Vehicle Number: ")
        parking.exit_vehicle(vehicle_no)

    elif choice == "3":
        parking.available_slots()

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")