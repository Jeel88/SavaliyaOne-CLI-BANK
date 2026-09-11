accounts = {}
transactions = {}

def generate_account_number():
    if len(accounts)==0:
        return 1001

    return max(accounts) + 1

def create_account():
    print("\n-------Create Account-------")
    name=input("\nEnter your name: ")
    age=int(input("Enter your age: "))
    deposit = float(input("Enter initial deposit: ₹"))
    pin = input("Create a 4-digit PIN: ")
    account_number = generate_account_number()


    account={"name":name,
             "age":age,
             "deposit":deposit,
             "pin":pin}
    accounts[account_number] = account
    transactions[account_number] = []

    print("\nAccount created successfully!")
    print("Account Number:", account_number)

    return account_number

def login():
    print("\n--- LOGIN ---")

    account_number = int(input("Enter account number: "))
    pin = input("Enter PIN: ")

    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", accounts[account_number]["name"])
            return account_number
        else:
            print("\nIncorrect PIN.")
    else:
        print("\nAccount not found.")

    return None

def credit_money(account_number):
    print("\n--- CREDIT MONEY ---")

    amount = float(input("Enter amount to credit: ₹"))

    if amount <= 0:
        print("\nAmount must be greater than 0.")
        return

    accounts[account_number]["balance"] += amount
    transactions[account_number].append({
        "type": "Credit",
        "amount": amount })

    print("\n₹", amount, "credited successfully!")
    print("New Balance: ₹", accounts[account_number]["balance"])

def debit_money(account_number):
    print("\n--- DEBIT MONEY ---")

    amount = float(input("Enter amount to debit: ₹"))

    if amount <= 0:
        print("\nAmount must be greater than 0.")
        return

    if amount > accounts[account_number]["balance"]:
        print("\nInsufficient balance.")
        return

    accounts[account_number]["balance"] -= amount
    transactions[account_number].append({
        "type": "Debit",
        "amount": amount })

    print("\n₹", amount, "debited successfully!")
    print("New Balance: ₹", accounts[account_number]["balance"])    