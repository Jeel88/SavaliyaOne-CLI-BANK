from create_account import create_account, login
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
    login()
elif(choice=="3"):
    print("\nThanks for choosing SAVALIYA ONE :)")
else:
    print("\n❌ Invalid choice.")
