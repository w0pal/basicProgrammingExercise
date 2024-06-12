from banksystem import BankSystem

def deposit(bank_system):
    account_number = input("Enter account number: ")
    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount.")
        return

    success, message = bank_system.deposit(account_number, amount)
    print(message)
