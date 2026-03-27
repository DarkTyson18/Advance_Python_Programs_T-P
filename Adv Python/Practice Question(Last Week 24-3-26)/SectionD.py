# 6. Write a program:
#  - Simulate login system
#  - Use file to store username/password
# File name to store user data
FILE_NAME = "users.txt"

try:
    choice = input("Do you want to Register (R) or Login (L)? ").lower()

    if choice == 'r':
        username = input("Enter new username: ")
        password = input("Enter new password: ")

        # Save to file
        with open(FILE_NAME, "a") as f:
            f.write(username + "," + password + "\n")

        print("Registration Successful!")

    elif choice == 'l':
        username = input("Enter username: ")
        password = input("Enter password: ")

        found = False

        # Read file
        with open(FILE_NAME, "r") as f:
            for line in f:
                user, pwd = line.strip().split(",")
                if user == username and pwd == password:
                    found = True
                    break

        if found:
            print("Login Successful!")
        else:
            print("Invalid Username or Password!")

    else:
        print("Invalid choice!")

except FileNotFoundError:
    print("Error: User file not found. Please register first.")





# 17. Exception Handling:
#  - Create custom exception "InvalidAgeError"
#  - Raise error if age < 18

"""class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    
    if age < 18 and age<100:
        raise InvalidAgeError("Age must be 18 or above!")
    
    print("You are eligible.")

except InvalidAgeError as e:
    print("Error:", e)"""