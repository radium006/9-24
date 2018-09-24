class Account_Management:
    def __init__(self):
        

class Account:
    def __init__(self, first_name, last_name, middle_name, account_type):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.account_type = account_type
        self.balance = 100
        self.status = 'Opened'

    def addFunds(self, funds):
        self.balance = self.balance + funds
    
    def withdrawFunds(self, funds):
        if(self.balance < funds):
            print("ACCOUNT OVERDRAWN, OVERDRAFT FEE APPLIED")
            self.balance = self.balance - funds - 35
        else:
            self.balance = self.balance - funds
    
    def transferFunds(self, other_account, funds):
        self.withdrawFunds(funds)
        other_account.addFunds(funds)

    def __repr__(self):
        return "{0} {1} {2}'s {3} Account, current balance: ${4} ".format(self.first_name,self.middle_name,self.last_name,self.account_type, self.balance)

print("Welcome to Kev's bank account simulator!")
print("Initializing a started Checking and Savings account with initial balance of $100...")
first = input('Enter first name: ')
middle = input('Enter middle name: ')
last = input('Enter last name: ')

account1 = Account(first,last,middle,'Checking')
account2 = Account(first,last,middle,'Savings')

while True:
    choice = input("What would you like to do? Press T to trasfer funds, Press 'D' to display account status, Press 'Q to quit; ").lower()

    if choice == 'q':
        break
    elif choice == 'd':
        print(account1)
        print(account2)



    