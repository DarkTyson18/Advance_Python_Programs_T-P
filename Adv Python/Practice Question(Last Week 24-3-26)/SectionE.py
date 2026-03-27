# 18. Create a Tkinter form:
#  - Name input
#  - Submit button
#  - Show entered name
"""from tkinter import *

def submit():
    name = entry.get()
    label_result.config(text="Hello, " + name)

root = Tk()
root.title("Simple Form")
root.geometry("300x200")

Label(root, text="Enter Name:").pack(pady=10)
entry = Entry(root)
entry.pack()

Button(root, text="Submit", command=submit).pack(pady=10)

label_result = Label(root, text="")
label_result.pack()

root.mainloop()"""

# 19. Python + SQL:
#  - Connect database
#  - Create table Student
#  - insert 3 records
#  - Fetch and display all

import mysql.connector
con = mysql.connector.connect(
  port=3306,
  host ="localhost",        
  user ="root",
  password ="Shashi@11906",
  database='giet'
)

# print(con)
cur = con.cursor()

query = "select * from student"
query = "select * from student where name='shashi'"
query = "select * from student where age=21"


cur.execute(query)
  
myresult = cur.fetchall()
for x in myresult:
  print(x)

con.close()



# 20. Build mini project:
#  STUDENT MANAGEMENT SYSTEM
#  Features:
#  - Add student
#  - View student
#  - Delete student
#  - Store data in file or database
"""filename = "students.txt"

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")

    with open(filename, "a") as f:
        f.write(name + "," + age + "\n")

    print("Student added!")

def view_students():
    try:
        with open(filename, "r") as f:
            print("\nStudent List:")
            for line in f:
                name, age = line.strip().split(",")
                print("Name:", name, "| Age:", age)
    except FileNotFoundError:
        print("No data found!")

def delete_student():
    name_to_delete = input("Enter name to delete: ")

    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(filename, "w") as f:
            for line in lines:
                if not line.startswith(name_to_delete + ","):
                    f.write(line)

        print("Student deleted!")

    except FileNotFoundError:
        print("File not found!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")"""