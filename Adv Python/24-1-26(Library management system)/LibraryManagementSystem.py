library_inventory = {
    "B001": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "available": True
    },
    "B002": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "available": False  # Book is currently issued
    },
    "B003": {
        "title": "1984",
        "author": "George Orwell",
        "available": True
    },
    "B004": {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "available": False
    }
}



def Show_Available_Book():
    print(library_inventory)
        
    
# Add Student
def Add_Book():
    Book_id = input("Enter Book id: ")
    Book_title = input("Enter Book title: ")
    Book_author = input("Enter Book author: ")
    Availability = bool(input("Enter the book Availability"))

    library_inventory[Book_id] = {"title": Book_title, "author": Book_author, "available": Availability}
    print("Book added successfully.")

# Add Course
def Remove_Book():
    remove_Book_id = input("Enter Book id to remove it from the library system: ")
    if remove_Book_id in library_inventory:
        library_inventory.remove(remove_Book_id)
        print("Book has REmove Successfully ")
    else:
        print("Enter Book details is not Available in the Library")
       

# Enrol Student
def Update_Book():
    Enter_Present_Book_id = input("Enter Book id you want to Update: ")
    if Enter_Present_Book_id in library_inventory:
        Book_id_new = input("Enter new Book id: ")
        Book_title_new = input("Enter new Book title: ")
        Book_author_new = input("Enter new Book author: ")
        Availability_new = bool(input("Enter the book Availability"))
        library_inventory[Enter_Present_Book_id].replace(library_inventory[Book_id_new])
        library_inventory[Book_id_new]={"title": Book_title_new, "author": Book_author_new, "available": Availability_new}
        print("Book has Updated Successfully ")
    else:
        print("Entered Book id which you want to Update is not available in th esystem")


def Borrow_Book():
    Borrow_Book_id = input("Enter the Book id you want to Borrow: ")

    if Borrow_Book_id in library_inventory:
        library_inventory[Borrow_Book_id].update(available=False)
        print("Book Borrowed Successfully")
    else:
        print("Enter the Book id is not available")
 


print("Welcome to Ai Library\n")

# Main Menu
while True:
    print("0. Show Available books")
    print("1. ADD BOOK to Library system")
    print("2. REMOVE BOOK from Library system")
    print("3. UPDATE BOOK in Library system")
    print("4. Borrow Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        Show_Available_Book()
    elif choice == "1":
        Add_Book()
    elif choice == "2":
        Remove_Book()
    elif choice == "3":
        Update_Book()
    elif choice == "4":
        Borrow_Book() 
    elif choice == "5":   
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")