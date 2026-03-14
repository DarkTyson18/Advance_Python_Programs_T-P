#A system to search,book,and cancel flight tickets
#handle exception such as seat not available, invalid passenger details, payment failure.


indigo_airline={"Flight name":"Indigo","Fligth no":"IN1011","Source":"Delhi","Destination":"Mumbai","Price per ricket":5000,"Seats Available":None}
indigo_airlines_seats= {
"A1": None, "A2": None, "A3": None, "A4": None, "A5": None,"A6": None, "A7": None, "A8": None, "A9": None, "A10": None,
"A11": None, "A12": None, "A13": None, "A14": None, "A15": None,"A16": None, "A17": None, "A18": None, "A19": None, "A20": None,
"A21": None, "A22": None, "A23": None, "A24": None, "A25": None,"A26": None, "A27": None, "A28": None, "A29": None, "A30": None,
"A31": None, "A32": None, "A33": None, "A34": None, "A35": None,"A36": None, "A37": None, "A38": None, "A39": None, "A40": None,
"A41": None, "A42": None, "A43": None, "A44": None, "A45": None,"A46": None, "A47": None, "A48": None, "A49": None, "A50": None
}

Air_india_airlines={"Flight name":"Air India","Fligth no":"AI2011","Source":"Delhi","Destination":"Banglore","Price per ricket":6000,"Seats Available":None}
Air_india_airlines_seats= {
"B1": None, "B2": None, "B3": None, "B4": None, "B5": None,"B6": None, "B7": None, "B8": None, "B9": None, "B10": None,
"B11": None, "B12": None, "B13": None, "B14": None, "B15": None,"B16": None, "B17": None, "B18": None, "B19": None, "B20": None,
"B21": None, "B22": None, "B23": None, "B24": None, "B25": None,"B26": None, "B27": None, "B28": None, "B29": None, "B30": None,
"B31": None, "B32": None, "B33": None, "B34": None, "B35": None,"B36": None, "B37": None, "B38": None, "B39": None, "B40": None,
"B41": None, "B42": None, "B43": None, "B44": None, "B45": None,"B46": None, "B47": None, "B48": None, "B49": None, "B50": None
}


bookings_details = {"P1":None,"P2":None,"P3":None,"P4":None,"P5":None,"P6":None,"P7":None,"P8":None,"P9":None,"P10":None,}

#Custom Exceptions
class SeatNotAvailable(Exception):
    pass

class InvalidPassengerDetails(Exception):
    pass

class PaymentFailed(Exception):
    pass


class Flight:

    # def flight_delhi_to_mumbai(self):
        
    def display_indigo_detais(self):
        print(indigo_airline)

    def display_AirIndia_details(self):
        print(Air_india_airlines)


class Passenger:
    def __init__(self, name, age):
        if name == "" or age <= 0:
            raise InvalidPassengerDetails("Invalid passenger details!")
        


class booking_details:
     
     def Show_booking_details(self):
        print("Passanger Booking details : ")
        for key, val in bookings_details.items():
            if val != None:
                print(key, val)
            
        cnt=0
        for key, val in bookings_details.items():
            if val==None:
                cnt+=1
        if cnt==10:
            print("Their is no booking till now")
                


class make_payment:

    def make_payment(self,total_cost):

        if total_cost !=0:
            print("Amount you need to pay : ",total_cost)
            choice = input("Confirm payment of ₹" + str(total_cost) + "? (yes/no): ")
            if choice.lower() != "yes":
                raise PaymentFailed("Payment was not successful!")
            print("Payment successful!")
            total_cost=0

        else:
            print("Payment done already")


class FlightBookingSystem:
    
    def Book_indigo_ticket(self,total_cost):
        self.total_cost = total_cost
        pep=int(input("Enetr the number of people : "))
        i=1
        while(i<=pep):
            
            ind_details = {"name": None,"age": None,"seat": None,"Flight details" : None}
            name = input(f"Passenger {i} name: ")
            age = int(input(f"Passenger {i} age: "))
            passenger = Passenger(name, age)
            
            seat=input("Enter the seat number : ")
            if seat in indigo_airlines_seats:
                if indigo_airlines_seats[seat]==None:
                    indigo_airlines_seats[seat]="Occupied"

                    ind_details["name"]=name
                    ind_details["age"]=age
                    ind_details["seat"]=seat
                    ind_details["Flight details"]="Indigo , IN1011 , Delhi - Mumbai , Price - 5000"

                    for key in bookings_details:
                        if bookings_details[key]==None:
                            bookings_details[key]=ind_details
                            print("Seat's book successfully")
                            break
                            
                else:
                    raise SeatNotAvailable("Seat already full")
            else:
                print("Invlaid seat number")
             
            i=i+1

        self.total_cost += (pep*5000)  

        

    def Book_AirIndia_ticket(self,total_cost):
        self.total_cost = total_cost
        pep=int(input("Enetr the number of people : "))
        i=1
        while(i<=pep):
            ind_details = {"name": None,"age": None,"seat": None,"Flight details" : None}
            name = input(f"Passenger {i} name: ")
            age = int(input(f"Passenger {i} age: "))
            passenger = Passenger(name, age)
            seat=input("Enter the seat number : ")
            if seat in Air_india_airlines_seats:
                if Air_india_airlines_seats[seat]==None:
                    Air_india_airlines_seats[seat]="Occupied"

                    ind_details["name"]=name
                    ind_details["age"]=age
                    ind_details["seat"]=seat
                    ind_details["Flight details"]="Air-India , AI2011 , Delhi - Banglore , Price - 6000"

                    for key in bookings_details:
                        if bookings_details[key]==None:
                            bookings_details[key]=ind_details
                            print("Seat's book successfully")
                            break

                else:
                    raise SeatNotAvailable("Seat already full")
            else:
                print("Invlaid seat number")
               
            i=i+1

        self.total_cost += (pep*6000)
        
            

    def cancel_ticket(self,name):

        for key, val in bookings_details.items():

            if val != None and val["name"] == name:

                seat = val["seat"]

                if seat.startswith("A"):
                    indigo_airlines_seats[seat] = None

                elif seat.startswith("B"):
                    Air_india_airlines_seats[seat] = None

                bookings_details[key] = None

                print("Ticket cancelled successfully")
                return

    print("Passenger booking not found")


# -------- Main Program --------
system = FlightBookingSystem()
flg=Flight()
sbd=booking_details()
mp=make_payment()


total_cost = 0

while True:
    print("\n1.Search Flights")
    print("2.Book Ticket")
    print("3.Cancel Ticket")
    print("4.Show booking details")
    print("5.Proceed with payments")
    print("6.Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            src = input("Enter source: ")
            dest = input("Enter destination: ")

            if(src=="delhi" and dest=="mumbai"):
                seats_ava_in_indigo=0
                for k1,v1 in indigo_airlines_seats.items():
                    if v1==None:
                        seats_ava_in_indigo+=1
                indigo_airline["Seats Available"]=seats_ava_in_indigo
                flg.display_indigo_detais()

            if(src=="delhi" and dest=="banglore"):
                seats_ava_in_Air_India=0
                for k2,v2 in Air_india_airlines_seats.items():
                    if v2==None:
                        seats_ava_in_Air_India+=1
                Air_india_airlines["Seats Available"]=seats_ava_in_Air_India
                flg.display_AirIndia_details()

        elif choice == "2":

            print("1. Flight name : Indigo, Source : Delhi, Destination : Mumbai")
            print("2. Flight name : Air India, Source : Delhi, Destination : Banglore")
            choice=int(input("Enter your choice : "))
            if choice==1:
                system.Book_indigo_ticket(0)

            elif choice==2:
                system.Book_AirIndia_ticket(0)
        

        elif choice == "3":
            name = input("Enter the passenger name : ")
            system.cancel_ticket(name)

        elif choice=="4":
            sbd.Show_booking_details()

        elif choice == "5":
            mp=make_payment(system.total_cost)

        else:
            print("Invalid option!")

    except SeatNotAvailable as e:
        print("Error:", e)

    except InvalidPassengerDetails as e:
        print("Error:", e)

    except PaymentFailed as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected error:", e)