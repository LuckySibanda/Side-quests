import json

filename = 'source.txt'


class Bank:
    def __init__(self, name):
        self.name = name
        self.account_list = []
        self.account_dict = {}

    def add_account(self, new_account):
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                dictionary = json.loads(contents)

            for account_number, balance in dictionary.items():
                new_account = BankAccount(account_number, balance)
                new_account.account_number = account_number
                new_account.balance = balance

                self.account_list.append(new_account)
                self.account_dict[new_account.account_number] = new_account

        except FileNotFoundError:
            print("File Not Found")

    def list_of_accounts(self):
        for new_account in self.account_list:
            print(f"{new_account.account_number}: {new_account.balance}")

    def total_bank_balance(self):
        total_balance = sum(new_account.balance for new_account in self.account_dict.values())
        print(f"The Total Bank Balance is ${total_balance}")


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                dictionary = json.loads(contents)

            dictionary[self.account_number] += amount
            self.balance += amount

            with open(filename, 'w') as file:
                json.dump(dictionary, file)

        except FileNotFoundError:
            print("File Not Found!")


    def withdraw(self, amount):
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                dictionary = json.loads(contents)

                dictionary[self.account_number] -= amount
                self.balance -= amount

            with open(filename, 'w') as file:
                json.dump(dictionary, file)

        except FileNotFoundError:
            print("File Not Found!")


bank = Bank("FNB")

def deposit():
    print("===Depositing===\n")
    while True:
        account_number = input("Enter your account number (or 'q' to quit): ")
        if account_number == 'q':
            break
        amount = int(input("Enter the amount to deposit: "))

        
        for account in bank.account_list:
            if account.account_number == account_number:
                print(f"{account.account_number}: {account.balance}\n")
                account.deposit(amount)
                print(f"{account.account_number}: {account.balance}\n")
                break

def withdraw():
    print("===Withdrawing===\n")
    while True:
        account_number = input("Enter your account number (or 'q' to quit): ")
        if account_number == 'q':
            break
        amount = int(input("Enter the amount you want to withdraw: "))

        for account in bank.account_list:
            if account.account_number == account_number:
                # print(f"{account.account_number}: {account.balance}\n")
                # account.withdraw(amount)
                # print(f"{account.account_number}: {account.balance}\n")
                if account.balance >= amount:
                    account.withdraw(amount)
                elif account.balance < amount:
                    print("Insufficient balance for transaction")
                break


def transactionType():
    print("Choose the transaction you want to perform \n -Deposit\n -Withdraw")
    while True:
        transaction_type = input("Enter transaction type (or 'q' to quit): ")
        if transaction_type == 'q':
            break

        elif transaction_type.lower() == "withdraw":
            withdraw()
        elif transaction_type.lower() == "deposit":
            deposit()
        else:
            print("Enter valid value,")

    print("Thank You For Banking With FNB!")
        

bank.add_account(BankAccount("", 0))
transactionType()
# deposit()
# withdraw()
# bank.list_of_accounts()
# bank.total_bank_balance()