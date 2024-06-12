class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number):
        if account_number in self.accounts:
            return False, "Account already exists."
        self.accounts[account_number] = 0
        return True, "Account created successfully."

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return False, "Account does not exist."
        if amount <= 0:
            return False, "Deposit amount must be positive."
        self.accounts[account_number] += amount
        return True, "Deposit successful."

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return False, "Account does not exist."
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if self.accounts[account_number] < amount:
            return False, "Insufficient funds."
        self.accounts[account_number] -= amount
        return True, "Withdrawal successful."

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            return False, "Account does not exist."
        return True, self.accounts[account_number]
