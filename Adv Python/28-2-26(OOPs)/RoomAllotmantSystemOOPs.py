class RoomAllotment:
    def allocate_rooms(self,name,room_no):
        self.name = name
        self.room_no = room_no
        
        allocated_rooms = False
        for self.room_no in rooms:
            if rooms[self.room_no] is None:
                rooms[self.room_no] = name
                print(f"Room {self.room_no} allocated to {name}.")
                allocated = True
                break
        if not allocated:
            print("Sorry! All rooms are occupied.")
            
    
    def room_status(self):        
        for self.room_no, occupant in rooms.items():
            if occupant is None:
                print(f"Room {self.room_no}: Free")
            else:
                print(f"Room {self.room_no}: Occupied by {occupant}")    
                
        
    def remove_student(self,roomid):
        self.room_no = roomid
        if self.room_no in rooms is not None:
            print(f"Student {rooms[self.room_no]} removed from Room {self.room_no}.")
            rooms[self.room_no] = None
        else:
            print("room is already free.")                            
            
rooms = {
    101: None,
    102: None,
    103: None,
    104: None,
    105: None
}  
while True:
    print("\n Hostel Room Allocation")
    print("1.Allocate Room")
    print("2.View Room Status")
    print("3.Remove Student from Room")
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj = RoomAllotment()
        name=input("Enter your name : ")
        for k,v in rooms.items():
            if rooms[k]==None:
                obj.allocate_rooms(name,k)
                break
    elif choice == 2:
        print("\nRoom Status:")   
        obj.room_status()
    elif choice == 3:
        roomid = int(input("enter the room number of student to remove:"))
        obj.remove_student(roomid)
    elif choice == 4:
         print("Exiting the program.")
         break        
    else:
         print("Invalid choice.")
