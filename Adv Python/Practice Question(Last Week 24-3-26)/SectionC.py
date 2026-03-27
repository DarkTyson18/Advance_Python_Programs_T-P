# 9. Write a program to:
#  - Take input string
#  - Count vowels and consonants
"""str=input("Enter the string : ")
vowels="aeiouAEIOU"
vow_count=0
cons_count=0

for c in str:
    if c in vowels:
        vow_count += 1
    else:
        cons_count+=1

print("Total Vowels :",vow_count)
print("Total Consonants :",cons_count)"""

# 10. Write a program to:
#  - Read a file
#  - Count number of lines, words and characters
"""FILE_NAME="File.txt"

content=input("Enter something into the file : \n")

with open(FILE_NAME, "a") as f:
    f.write(content+"\n")

try:
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        word_count += len(line.split())  
        char_count += len(line.replace(" ", "").replace("\n", ""))           

    print("Number of lines:", line_count)
    print("Number of words:", word_count)
    print("Number of characters:", char_count)

except FileNotFoundError:
    print("Error: File not found!")"""


# 11. Write a program:
#  - Create a class BankAccount
#  - Methods: deposit, withdraw, check balance
"""class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)


acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(300)
acc.check_balance()"""

# 12. Write a program:
#  - Accept list of numbers
#  - Remove duplicates
#  - Sort it without using sort()

"""nums = [5,2,8,4,3,9,5,1]
print("Input list : ",nums)

unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

unique_nums.sort()

print("Sorted list without duplicates:", unique_nums)"""

# 13. Write a program using lambda + map + filter:
#  - Square only even numbers from list

"""nums = list(map(int, input("Enter numbers: ").split()))

result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print("Squared even numbers:", result)"""