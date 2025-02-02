class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Replenishment:", amount,"₸")
        print("Balance:", self.balance,"₸")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Error: Insufficient funds. Current balance:",self.balance,"₸")
        else:
            self.balance -= amount
            print("Withdrawal of", amount,"₸.")
            print("Remainder:",self.balance, "₸")

# Account name
owner = input("Please enter your name:" )
balance = 10000
account = BankAccount(owner,balance)
# Replenishment
amount = int(input("Replenishment:"))
account.deposit(amount)
# Withdrawl
withdrawl = int(input("How much you want withdraw:"))
account.withdraw(withdrawl)


