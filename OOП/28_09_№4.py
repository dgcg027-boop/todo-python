class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = amount + self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance = self.balance - amount

    def info(self):
        print(f"{self.owner}: {self.balance} руб.")


account = BankAccount("Степан", 1000)
account.deposit(500)
account.info()
account.withdraw(2000)
account.info()