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
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        allocated = False
        for room_no in rooms:
            if rooms[room_no] is None:
                rooms[room_no] = name
                print(f"Room {room_no} allocated to {name}.")
                allocated = True
                break
        if not allocated:
            print("Sorry! All rooms are occupied.")
    elif choice == 2:
        print("\nRoom Status:")
        for room_no, occupant in rooms.items():
            if occupant is None:
                print(f"Room {room_no}: Free")
            else:
                print(f"Room {room_no}: Allocated to {occupant}")
    else:
        print("Invalid choice, Try again.")