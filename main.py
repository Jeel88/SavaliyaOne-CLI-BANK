from database import create_database

from account import (
    create_account,
    login,
    check_balance,
    credit_money,
    debit_money,
    transfer_money,
    transaction_history,
    account_details,
    account_analytics,
    change_pin
)

create_database()

while True:
    print("\n" + "=" * 50)
    print("              SAVALIYAONE")
    print("                 CLI BANK")
    print("=" * 50)

    print("\n1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        create_account()

    elif choice == "2":
        logged_in_account = login()

        if logged_in_account is not None:
            while True:
                print("\n--- BANKING DASHBOARD ---")
                print("1. Check Balance")
                print("2. Credit Money")
                print("3. Debit Money")
                print("4. Transfer Money")
                print("5. Account Details")
                print("6. Transaction History")
                print("7. Transaction Analytics")
                print("8. Change PIN")
                print("9. Logout")

                dashboard_choice = input("\nEnter your choice: ").strip()

                if dashboard_choice == "1":
                    check_balance(logged_in_account)

                elif dashboard_choice == "2":
                    credit_money(logged_in_account)

                elif dashboard_choice == "3":
                    debit_money(logged_in_account)

                elif dashboard_choice == "4":
                    transfer_money(logged_in_account)

                elif dashboard_choice == "5":
                    account_details(logged_in_account)

                elif dashboard_choice == "6":
                    transaction_history(logged_in_account)

                elif dashboard_choice == "7":
                    account_analytics(logged_in_account)

                elif dashboard_choice == "8":
                    change_pin(logged_in_account)

                elif dashboard_choice == "9":
                    print("\nLogged out successfully.")
                    break

                else:
                    print("\nInvalid choice. Please select 1-9.")

    elif choice == "3":
        print("\nThank you for using SAVALIYAONE CLI BANK.")
        break

    else:
        print("\nInvalid choice. Please select 1-3.")