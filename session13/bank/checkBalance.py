from banksystem import BankSystem

def check_balance(bank_system):
    account_number = input("Enter account number: ")
    success, balance = bank_system.check_balance(account_number)
    if success:
        print(f"Balance for account {account_number}: {balance}")
    else:
        print(balance)
