class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self, amount):
        if amount>0:
            self.balance = self.balance+amount
            print(f'the deposited amount is {amount}')
        else:
            print("cannot add negative value")

    def withdraw(self, withdraw):
        if self.balance<withdraw:
            print("Your bank account does not have the sufficient balance to withdraw the amount you entered")
        else:
            self.balance=self.balance-withdraw
            return withdraw

    def display(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added to {self.owner}'s account.")
        return interest

customer1= BankAccount("akash", 4000)
balance=customer1.display()
print(f'the initial balance is {balance}')
customer1.deposit(4000)
balance1=customer1.display()
print(f'the new balance is {balance1}')
withdrawed=customer1.withdraw(2000)
print(f'the mount withdrawed by customer1 is {withdrawed}')

balance2=customer1.display()
print(f'the new balance is {balance2}')

savings = SavingsAccount("Akash", 5000, interest_rate=0.1)
savings.display()
savings.add_interest()
savings.display()