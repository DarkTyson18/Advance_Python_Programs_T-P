
#List based transaction system
print("Welcome to SBI")
pin=5555
balance=10000
response=0
tran_his=[]
i=0
while i<3:
    ent_pin=int(input("Enter your pin : "))
    if(ent_pin==pin):
        print("\n1.Deposit")
        print("\n2.withdraw")
        print("\n3.check balance")
        print("\n4.transaction history")
        print("\n5.exit")

        response=int(input("Tell your Response : "))

        if(response==1):
            Ent_amt=int(input("Enter the amount you want to deposite : "))
            balance = balance+Ent_amt
            tran_his.append("Deposited "+str(Ent_amt))
            print("Amount Deposited")

        elif(response==2):
            Ent_withdraw=int(input("Enter the amount you want to Withdraw : "))
        
            if(Ent_withdraw  >  balance):
                print("You have less balance then entered Withdrawal amount")
            else:
                balance = balance - Ent_withdraw
                tran_his.append("Withdraw "+str(Ent_withdraw))
                print("Amount withdraw")
           

        elif(response==3):
            print("Available balance : ",balance)
           
    
        elif(response==4):
            print("Your transaction history : ")
            for i in tran_his:
                print(" ",i)
           
    
        elif(response==5):
            print("Thanku")


        break
    else: 
        print("Wrong pin, Retry")
    i=i+1


    
print("Thanks for choosing our services")
