# Empty dictionaries
pin=5555

response=0
tran_his=[]

# Add Student

def Deposite_amount():
    Ent_amt=int(input("Enter the amount you want to deposite : "))
    balance = balance+Ent_amt
    tran_his.append("Deposited "+str(Ent_amt))
    print("Amount Deposited")
2
# Add Course
def Withdraw_amount():
    Ent_withdraw=int(input("Enter the amount you want to Withdraw : "))
        
    if(Ent_withdraw  >  balance):
        print("You have less balance then entered Withdrawal amount")
    else:
        balance = balance - Ent_withdraw
        tran_his.append("Withdraw "+str(Ent_withdraw))
        print("Amount withdraw")

# Enrol Student
def Check_the_balance():
    print("Available balance : ",balance)

# View Student Report
def Show_transaction_history():
    print("Your transaction history : ")
    for i in tran_his:
        print(" ",i)

# Main Menu

print("Welcome to SBI")
global balance
min_balance=int(input("Enter the minimum balance  : "))
balance=balance+min_balance


ent_pin=int(input("Enter your pin : "))

i=0
while i<3:

    if(ent_pin==pin):
        print("1.Deposit")
        print("2.withdraw")
        print("3.check balance")
        print("4.transaction history")
        print("5.exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Deposite_amount()
        elif choice == "2":
            Withdraw_amount()
        elif choice == "3":
            Check_the_balance()
        elif choice == "4":
            Show_transaction_history()    
        elif choice == "5":
            print("Exiting program...")
            break
    else:
        print("Invalid choice.")
    i=i+1