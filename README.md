Download latest version of Python from https://www.python.org/downloads/
Get an IDE like VSCode of Pycharm

The program is an implementation of a basic banking system using classes and JSON file storage. It allows users to create bank accounts, deposit and withdraw funds, and view the account balance.

Here's a summary of the code:

The code defines two classes: Bank and BankAccount. The Bank class represents a bank and has methods for adding accounts, listing accounts, and calculating the total bank balance. The BankAccount class represents a bank account and has methods for depositing and withdrawing funds.

The Bank class has an add_account method that reads account information from a JSON file and creates BankAccount objects for each account. The account information is stored in account_list (a list of BankAccount objects) and account_dict (a dictionary where the account number is the key and the BankAccount object is the value).

The Bank class also has a list_of_accounts method that displays the account number and balance for each account in the account_list.

The Bank class has a total_bank_balance method that calculates and displays the total balance of all accounts in the bank.

The BankAccount class has an __init__ method that initializes the account number and balance.

The BankAccount class has deposit and withdraw methods that update the account balance. These methods read the account information from the JSON file, perform the deposit or withdrawal operation, and update the JSON file with the new balance.

The code creates an instance of the Bank class named bank with the name "FNB" (First National Bank).

The code defines deposit and withdraw functions that allow users to deposit or withdraw funds from their accounts. These functions prompt the user for an account number and amount, find the corresponding account in the bank instance, perform the deposit or withdrawal operation, and display the updated balance.

The transactionType function prompts the user to choose a transaction type (deposit or withdraw) and calls the deposit or withdraw function accordingly. The user can perform multiple transactions until they choose to quit.

Finally, the code adds a default account to the bank using bank.add_account(BankAccount("", 0)) and calls the transactionType function to start the banking system.

To use the code, you need to have a JSON file named 'source.txt' in the same directory as the script. The JSON file should contain account information in the format: {"account_number": balance}. For example: {"12345": 1000, "67890": 500}.


README is going to be updated to be more detailed later

STill working on the program to include error more error handling, testing and overall improve the program