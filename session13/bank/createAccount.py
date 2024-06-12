from banksystem import BankSystem

def create_account(bank_system):
    account_number = input("Enter new account number: ")
    success, message = bank_system.create_account(account_number)
    print(message)
