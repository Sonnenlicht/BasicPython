#! python3

from classbank import BankAccount
mary_account = BankAccount()
mary_account.deposit(100)
dana_account = BankAccount()
mary_account.transfer(dana_account, 20)
mary_account.balance
dana_account.balance
mary_account.transactions()
