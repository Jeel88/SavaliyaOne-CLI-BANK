accounts = {}
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

    print("\nAccount created successfully!")
    print("Account Number:", account_number)

    return account_number
