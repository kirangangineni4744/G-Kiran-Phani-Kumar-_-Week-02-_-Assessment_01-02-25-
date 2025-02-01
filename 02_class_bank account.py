class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print(f"Deposited amount:{amount}, Updated balance:{self.balance}")
        else:
            print("Invalid")

    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance=self.balance-amount
            print(f"Withdrawn amount:{amount}, Updated balance:{self.balance}")
        else:
            print("Insufficient balance")

print("Enter initial balance:")
initial_balance=int(input())
customer_account=BankAccount(initial_balance)

print("Enter the amount to deposit:")
amount=int(input())
customer_account.deposit(amount)

print("Enter the amount to withdraw:")
amount = int(input())
customer_account.withdraw(amount)
