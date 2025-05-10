class Account:
    def __init__(self, name, balance=0):
        self.__account_name = name
        self.__account_balance = 0
        self.set_balance(balance)

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

    def set_balance(self, value):
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value

    def set_name(self, value):
        self.__account_name = value

    def __str__(self):
        return f"Account name = {self.get_name()} | Account Balance = {self.get_balance(): .2f}"

class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name):
        super().__init__(name, self.MINIMUM)
        self.__deposit_count = 0

    def apply_interest(self):
        if self.__deposit_count > 0 and self.__deposit_count % 5 == 0:
            interest = self.get_balance() * self.RATE
            self.set_balance(self.get_balance() + interest)

    def deposit(self, amount):
        if amount > 0:
            success = super().deposit(amount)
            if success:
                self.__deposit_count += 1
                self.apply_interest()
                return True
        return False

    def withdraw(self, amount):
        if amount > 0 and (self.get_balance() - amount) >= self.MINIMUM:
            return super().withdraw(amount)
        return False

    def set_balance(self, value):
        if value < self.MINIMUM:
            super().set_balance(self.MINIMUM)
        else:
            super().set_balance(value)

    def __str__(self):
        return f"Saving Account: Account Name = {self.get_name()}, Account Balance: ${self.get_balance():.2f}"


def get_bank_total(accounts):
    total = 0
    for account in accounts:
        total += account.get_balance()
    return total
