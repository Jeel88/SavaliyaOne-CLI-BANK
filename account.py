from database import (
    insert_account,
    get_next_account_number,
    get_account,
    update_balance,
    insert_transaction,
    get_transactions,
    update_pin,
    transfer_funds
)

accounts = {}
transactions = {}


def create_account():
    print("\n------- Create Account -------")

    name = input("\nEnter your name: ")
    age = int(input("Enter your age: "))
    deposit = float(input("Enter initial deposit: ₹"))
    pin = input("Create a 4-digit PIN: ")

    account_number = get_next_account_number()

    insert_account(
        account_number,
        name,
        age,
        pin,
        deposit
    )

    if deposit > 0:
        insert_transaction(
            account_number,
            "Initial Deposit",
            deposit
        )

    accounts[account_number] = {
        "name": name,
        "age": age,
        "balance": deposit,
        "pin": pin
    }

    print("\nAccount created successfully!")
    print("Account Number:", account_number)
    print("Initial Balance: ₹", deposit)

    return account_number


def login():
    print("\n--- LOGIN ---")

    account_number = int(input("Enter account number: "))
    pin = input("Enter PIN: ")

    account = get_account(account_number)

    if account is None:
        print("\nAccount not found.")
        return None

    name = account[0]
    age = account[1]
    stored_pin = account[2]
    balance = account[3]

    if stored_pin == pin:
        print("\nLogin successful!")
        print("Welcome,", name)

        accounts[account_number] = {
            "name": name,
            "age": age,
            "balance": balance,
            "pin": stored_pin
        }

        return account_number
    else:
        print("\nIncorrect PIN.")
        return None


def check_balance(account_number):
    print("\n--- CHECK BALANCE ---")
    account = get_account(account_number)
    if account:
        balance = account[3]
        accounts[account_number]["balance"] = balance
        print("Current Balance: ₹", balance)
    else:
        print("Account not found.")


def credit_money(account_number):
    print("\n--- CREDIT MONEY ---")

    amount = float(input("Enter amount to credit: ₹"))

    if amount <= 0:
        print("\nAmount must be greater than 0.")
        return

    account = get_account(account_number)
    current_balance = account[3]

    new_balance = current_balance + amount

    update_balance(account_number, new_balance)
    insert_transaction(account_number, "Credit", amount)

    accounts[account_number]["balance"] = new_balance

    print("\n₹", amount, "credited successfully!")
    print("New Balance: ₹", new_balance)


def debit_money(account_number):
    print("\n--- DEBIT MONEY ---")

    account = get_account(account_number)
    current_balance = account[3]

    amount = float(input("Enter amount to debit: ₹"))

    if amount <= 0:
        print("\nAmount must be greater than 0.")
        return

    if amount > current_balance:
        print("\nInsufficient balance.")
        return

    new_balance = current_balance - amount

    update_balance(account_number, new_balance)
    insert_transaction(account_number, "Debit", amount)

    accounts[account_number]["balance"] = new_balance

    print("\n₹", amount, "debited successfully!")
    print("New Balance: ₹", new_balance)


def transfer_money(account_number):
    print("\n--- TRANSFER MONEY ---")

    account = get_account(account_number)
    current_balance = account[3]

    receiver_acc = int(input("Enter recipient account number: "))

    if receiver_acc == account_number:
        print("\nYou cannot transfer money to your own account.")
        return

    receiver = get_account(receiver_acc)
    if receiver is None:
        print("\nRecipient account not found.")
        return

    print("Recipient Name:", receiver[0])
    amount = float(input("Enter transfer amount: ₹"))

    if amount <= 0:
        print("\nAmount must be greater than 0.")
        return

    if amount > current_balance:
        print("\nInsufficient balance.")
        return

    transfer_funds(account_number, receiver_acc, amount)

    accounts[account_number]["balance"] = current_balance - amount

    print("\n₹", amount, "transferred successfully to Account #", receiver_acc)
    print("Remaining Balance: ₹", accounts[account_number]["balance"])


def transaction_history(account_number):
    print("\n--- TRANSACTION HISTORY ---")

    transaction_list = get_transactions(account_number)

    if len(transaction_list) == 0:
        print("No transactions yet.")
        return

    for transaction in transaction_list:
        print("Type:", transaction[0])
        print("Amount: ₹", transaction[1])
        print("-------------------------")


def account_details(account_number):
    print("\n--- ACCOUNT DETAILS ---")

    account = get_account(account_number)
    if account:
        name = account[0]
        age = account[1]
        balance = account[3]

        print("Account Number:", account_number)
        print("Name:", name)
        print("Age:", age)
        print("Balance: ₹", balance)


def account_analytics(account_number):
    print("\n--- TRANSACTION ANALYTICS ---")

    transaction_list = get_transactions(account_number)

    if len(transaction_list) == 0:
        print("No transactions available for analysis.")
        return

    total_txns = len(transaction_list)
    total_amount = sum(t[1] for t in transaction_list)

    print("Total Transactions:", total_txns)
    print("Total Transaction Volume: ₹", total_amount)


def change_pin(account_number):
    print("\n--- CHANGE PIN ---")

    account = get_account(account_number)
    if not account:
        print("Account not found.")
        return

    current_pin = input("Enter current 4-digit PIN: ")
    if current_pin != account[2]:
        print("\nIncorrect current PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")
    update_pin(account_number, new_pin)
    accounts[account_number]["pin"] = new_pin
    print("\nPIN updated successfully!")
