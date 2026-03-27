#simulate real time transaction between bank account.
#handle error like overdraft,transaction timeout, incorrect account number.

import time

class OverdraftError(Exception):
    pass

class TransactionTimeoutError(Exception):
    pass

class InvalidAccountNumberError(Exception):
    pass


class Bank:
    def __init__(self):
        self.accounts = {}   

    
    def create_account(self, acc_no, balance):
        self.accounts[acc_no] = balance
        print("Account created:", acc_no)

    
    def transfer(self, sender, receiver, amount):
        try:
            start_time = time.time()

            if sender not in self.accounts or receiver not in self.accounts:
                raise InvalidAccountNumberError("Incorrect account number.")

            if self.accounts[sender] < amount:
                raise OverdraftError("Insufficient balance.")

            
            time.sleep(2)

            if time.time() - start_time > 5:
                raise TransactionTimeoutError("Transaction timed out.")

            self.accounts[sender] -= amount
            self.accounts[receiver] += amount

            print("Transaction successful:", amount, "transferred.")

        except Exception as e:
            print("Error:", e)


    def display_accounts(self):
        print("\nAccount Details:")
        for acc, bal in self.accounts.items():
            print("Account:", acc, "Balance:", bal)



bank = Bank()

bank.create_account("A101", 5000)
bank.create_account("A102", 3000)

bank.transfer("A101", "A102", 1000)

bank.display_accounts()