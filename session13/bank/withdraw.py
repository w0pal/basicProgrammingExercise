from banksystem import BankSystem

def withdraw(bank_system):
    account_number = input("Enter account number: ")
    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount.")
        return

    success, message = bank_system.withdraw(account_number, amount)
    print(message)
