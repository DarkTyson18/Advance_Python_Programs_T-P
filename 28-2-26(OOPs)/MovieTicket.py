#check showtimes, book tickets, select seats, and print
#class movie_ticket:

class MovieTicket:

    def __init__(self):

        self.movie_name_day_and_time = {"Avengers-Endgame": {"Sunday", "8:00 - 12:00PM"}}

        self.people=[]
        self.number_of_people=[]
        self.seats=[]
        
        self.Premium_ticket = {
        'A1': None,'A2': None,'A3': None,'A4': None,'A5': None,'A6': None,'A7': None,'A8': None,'A9': None,'A10': None,
        'A11': None,'A12': None,'A13': None,'A14': None,'A15': None,'A16': None,'A17': None,'A18': None,'A19': None,'A20': None,
        'A21': None,'A22': None,'A23': None,'A24': None,'A25': None,'A26': None,'A27': None,'A28': None,'A29': None,'A30': None,
        'A31': None,'A32': None,'A33': None,'A34': None,'A35': None,'A36': None,'A37': None,'A38': None,'A39': None,'A40': None,
        'A41': None,'A42': None,'A43': None,'A44': None,'A45': None,'A46': None,'A47': None,'A48': None,'A49': None,'A50': None
        }

        self.standard_ticket = {
        'B1': None,'B2': None,'B3': None,'B4': None,'B5': None,'B6': None,'B7': None,'B8': None,'B9': None,'B10': None,
        'B11': None,'B12': None,'B13': None,'B14': None,'B15': None,'B16': None,'B17': None,'B18': None,'B19': None,'B20': None,
        'B21': None,'B22': None,'B23': None,'B24': None,'B25': None,'B26': None,'B27': None,'B28': None,'B29': None,'B30': None,
        'B31': None,'B32': None,'B33': None,'B34': None,'B35': None,'B36': None,'B37': None,'B38': None,'B39': None,'B40': None,
        'B41': None,'B42': None,'B43': None,'B44': None,'B45': None,'B46': None,'B47': None,'B48': None,'B49': None,'B50': None
        }

    # Show movie details
    def show_details(self):

        print(self.movie_name_day_and_time)

        cnt1 = 0
        cnt2 = 0

        for k1, v1 in self.Premium_ticket.items():
            if v1 == None:
                cnt1 += 1

        for k2, v2 in self.standard_ticket.items():
            if v2 == None:
                cnt2 += 1

        print(f"Premium ticket seat available : {cnt1}/{len(self.Premium_ticket)}")
        print(f"Standard ticket seat available : {cnt2}/{len(self.standard_ticket)}")


    # Book ticket
    def book_ticket(self):

        print("Which ticket you want to book --- 1.Premium_ticket --- 2.Standard_ticket")
        res = int(input("Enter your response : "))

        if res == 1:

            pep = int(input("Enter no.of people : "))

            i = 1
            while i <= pep:

                name = input("Enter your name : ")
                s_no = input(f"Enter the {i} seat number : ")

                if self.Premium_ticket[s_no] == None:
                    self.Premium_ticket[s_no] = "Occupied"
                    self.people.append(name)
                    self.seats.append(s_no)
                    self.number_of_people.append(pep)
                    i += 1
                else:
                    print("Selected seat is NOT available")

            print("Ticket booked successfully")


        elif res == 2:

            name = input("Enter your name : ")
            pep = int(input("Enter no.of people : "))

            i = 1
            while i <= pep:

                s_no = input(f"Enter the {i} seat number : ")

                if self.standard_ticket[s_no] == None:
                    self.standard_ticket[s_no] = "Occupied"
                    self.people.append(name)
                    self.seats.append(s_no)
                    self.number_of_people.append(pep)
                    i += 1
                else:
                    print("Selected seat is NOT available")

            print("Ticket booked successfully")

        else:
            print("Invalid input")


    
    def show_booking(self):
        print(self.movie_name_day_and_time)
        print(self.people)
        print(self.number_of_people)
        print(self.seats)




ticket = MovieTicket()

print("\nWelcome to Ilex Movie Hall")

while True:

    print("\n1. Check Show details")
    print("2. Book Ticket / select seat")
    print("3. Show Booked details")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ticket.show_details()

    elif choice == 2:
        ticket.book_ticket()

    elif choice == 3:
        ticket.show_booking()

    elif choice == 4:
        print("Thank you for visiting!")
        break

    else:
        print("Invalid choice.")