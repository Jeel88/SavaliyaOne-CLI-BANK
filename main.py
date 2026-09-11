from account import create_account, login, accounts
accounts={}

print("=" * 50)
print("                 SAVALIYA ONE")
print("                   CLI BANK")
print("=" * 50)

print("\n1. Create Account")
print("2. Login")
print("3. Exit")

choice = input("\nEnter your choice: ")
print("\nYou selected:", choice)

if(choice=="1"):
    account=create_account()

elif(choice=="2"):
    logged_in_account=login()
    if logged_in_account is not None:
        while True:
            print("\n--- BANKING DASHBOARD ---")
            print("1. Check Balance")
            print("2. Credit Money")
            print("3. Debit Money")
            print("4. Account Details")
            print("5. Logout")

            dashboard_choice = input("\nEnter your choice: ")
            if dashboard_choice == "1":
                    print(
                        "\nBalance: ₹",
                        accounts[logged_in_account]["balance"]
                    )

            elif dashboard_choice == "2":
                print("\nCredit Money")

            elif dashboard_choice == "3":
                print("\nDebit Money")

            elif dashboard_choice == "4":
                print("\nAccount Number:", logged_in_account)
                print("Name:", accounts[logged_in_account]["name"])
                print("Age:", accounts[logged_in_account]["age"])
                print("Balance: ₹", accounts[logged_in_account]["balance"])

            elif dashboard_choice == "5":
                print("\nLogged out successfully.")
                break

            else:
                print("\nInvalid choice.")

elif(choice=="3"):
    print("\nThanks for choosing SAVALIYA ONE :)")
else:
    print("\n❌ Invalid choice.")
