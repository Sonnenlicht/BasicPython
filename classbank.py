#! python3

"""Utilities and objects for managing bank accounts."""

class BankAccount:

    """Bank account including an account balance."""

    def __init__(self):
        """Open an account."""
        self.balance = 0
        self.transactionlist = [('OPEN', 0, 0)]
        print("Account opened.")
        self.print_balance()

    def deposit(self, amount):
        """Increase the account balance."""
        self.balance += amount
        self.transactionlist.append(('DEPOSIT', amount, self.balance))
        print("${} deposited.".format(amount))
        self.print_balance()

    def withdraw(self, amount):
        """Decrease the account balance."""
        self.balance -= amount
        self.transactionlist.append(('WITHDRAWAL', -amount, self.balance))
        print("${} withdrawn.".format(amount))
        self.print_balance()

    def transfer(self, other_account, amount):
        """Move money from our account to the given account."""
        self.withdraw(amount)
        other_account.deposit(amount)

    def print_balance(self):
        """Print the current account balance."""
        print("Account balance is ${}.".format(self.balance))

    def __str__(self):
        """Return a human-readable explanation of account."""
        return "Account with balance of ${}".format(self.balance)

    def __repr__(self):
        """Return a developer-readable representation of our account."""
        return "BankAccount(balance={})".format(self.balance)

    def transactions(self):
        """Return a list of transactions."""
        print(self.transactionlist)


class MinimumBalanceAccount(BankAccount):

    def withdraw(self,amount):
        if self.balance - amount <= 0:
            raise ValueError("Balance cannot be less than $0!")
        else:
            super.withdraw(amount)

#from classbank import MinimumBalanceAccount
my_account = MinimumBalanceAccount()
my_account.deposit(100)
my_account.withdraw(50)
my_account.withdraw(200)




            
        
