import sqlite3

DATABASE = "bank.db"


def create_database():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                pin TEXT,
                balance REAL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                account_number INTEGER,
                type TEXT,
                amount REAL
            )
        """)

        connection.commit()


def insert_transaction(account_number, transaction_type, amount):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO transactions
            (account_number, type, amount)
            VALUES (?, ?, ?)
        """, (account_number, transaction_type, amount))
        connection.commit()


def get_transactions(account_number):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT type, amount
            FROM transactions
            WHERE account_number = ?
        """, (account_number,))
        transactions = cursor.fetchall()
    return transactions


def get_next_account_number():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(account_number) FROM accounts")
        result = cursor.fetchone()[0]

    if result is None:
        return 1001

    return result + 1


def insert_account(account_number, name, age, pin, balance):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO accounts
            (account_number, name, age, pin, balance)
            VALUES (?, ?, ?, ?, ?)
        """, (account_number, name, age, pin, balance))
        connection.commit()


def get_account(account_number):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT name, age, pin, balance
            FROM accounts
            WHERE account_number = ?
        """, (account_number,))
        account = cursor.fetchone()
    return account


def update_balance(account_number, balance):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE accounts
            SET balance = ?
            WHERE account_number = ?
        """, (balance, account_number))
        connection.commit()


def update_pin(account_number, new_pin):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE accounts
            SET pin = ?
            WHERE account_number = ?
        """, (new_pin, account_number))
        connection.commit()


def transfer_funds(sender_acc, receiver_acc, amount):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, sender_acc))
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, receiver_acc))
        
        cursor.execute("""
            INSERT INTO transactions (account_number, type, amount)
            VALUES (?, ?, ?)
        """, (sender_acc, f"Transfer to Account #{receiver_acc}", amount))
        
        cursor.execute("""
            INSERT INTO transactions (account_number, type, amount)
            VALUES (?, ?, ?)
        """, (receiver_acc, f"Transfer from Account #{sender_acc}", amount))
        
        connection.commit()