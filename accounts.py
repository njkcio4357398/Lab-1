class Account:
    """Base class representing a bank account."""

    def __init__(self, name: str, balance: float = 0):
        self.__account_name = name
        self.__account_balance = 0
        self.set_balance(balance)

    def deposit(self, amount: float) -> bool:
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw amount if sufficient balance exists."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        """Return the current account balance."""
        return self.__account_balance

    def get_name(self) -> str:
        """Return the account holder's name."""
        return self.__account_name

    def set_balance(self, value: float) -> None:
        """Set the account balance, ensuring it is non-negative."""
        self.__account_balance = max(value, 0)

    def set_name(self, value: str) -> None:
        """Set the account holder's name."""
        self.__account_name = value

    def __str__(self) -> str:
        return f"Account name = {self.get_name()} | Account Balance = {self.get_balance():.2f}"


class SavingAccount(Account):
    """Subclass representing a savings account with interest and minimum balance rules."""

    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name: str):
        super().__init__(name, self.MINIMUM)
        self.__deposit_count = 0

    def apply_interest(self) -> None:
        """Apply interest every 5 deposits."""
        if self.__deposit_count > 0 and self.__deposit_count % 5 == 0:
            interest = self.get_balance() * self.RATE
            self.set_balance(self.get_balance() + interest)

    def deposit(self, amount: float) -> bool:
        """Deposit and track deposit count for interest application."""
        if amount > 0:
            success = super().deposit(amount)
            if success:
                self.__deposit_count += 1
                self.apply_interest()
                return True
        return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw only if minimum balance is preserved."""
        if amount > 0 and (self.get_balance() - amount) >= self.MINIMUM:
            return super().withdraw(amount)
        return False

    def set_balance(self, value: float) -> None:
        """Set balance with enforcement of minimum threshold."""
        if value < self.MINIMUM:
            super().set_balance(self.MINIMUM)
        else:
            super().set_balance(value)

    def __str__(self) -> str:
        return f"Saving Account: Account Name = {self.get_name()}, Account Balance: ${self.get_balance():.2f}"
