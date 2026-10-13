class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте")
        self.balance -= amount
        return self.balance


if __name__ == "__main__":
    account = BankAccount("Андрей", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Баланс {account.owner}: {account.balance}")
