# 🏦 SavaliyaOne CLI BANK

SavaliyaOne CLI BANK is a **Python-based Command-Line Banking System** designed to simulate basic banking operations through a terminal interface. Built with Python and SQLite3, it provides persistent data storage, account management, deposit/withdrawal handling, inter-account transfers, and detailed transaction records.

---

## ✨ Features

- 📝 **Account Creation**: Interactive registration with custom deposit and automated unique account numbers (starting from `1001`).
- 🔐 **User Authentication**: Secure 4-digit PIN login verification.
- 💾 **SQLite Database Persistence**: All account profiles, balances, PINs, and transaction histories persist automatically in `bank.db` across application restarts.
- 💵 **Credit & Debit Operations**: Instant balance updates for money deposits and withdrawals.
- 💸 **Inter-Account Money Transfer**: Transfer funds between two valid bank accounts with double-entry transaction history logging.
- 📊 **Transaction History**: Complete transaction log listing initial deposits, credits, debits, and transfers.
- 📈 **Transaction Analytics**: Visual summary of total transaction volume and account activity count.
- 🔑 **PIN Management**: Easily update your 4-digit PIN with verification.

---

## 🔄 Application Flow

```text
               +-----------------------+
               |  SAVALIYAONE CLI BANK |
               +-----------------------+
                           |
            +--------------+--------------+
            |                             |
    [1. Create Account]              [2. Login]
            |                             |
    Generates Account #             Validates PIN & Fetch DB
  Inserts Record into DB                   |
            +--------------+--------------+
                           |
             +---------------------------+
             |     BANKING DASHBOARD     |
             +---------------------------+
             | 1. Check Balance          |
             | 2. Credit Money           |
             | 3. Debit Money            |
             | 4. Transfer Money         |
             | 5. Account Details        |
             | 6. Transaction History    |
             | 7. Transaction Analytics  |
             | 8. Change PIN             |
             | 9. Logout                 |
             +---------------------------+
```

---

## 📁 Project Architecture

| File | Purpose |
| :--- | :--- |
| **`main.py`** | Main entry point containing menu loops and dashboard controls. |
| **`account.py`** | Beginner-friendly implementation of banking logic, user inputs, and dashboard actions. |
| **`database.py`** | SQLite database interface for account queries, transactions logging, and updates. |
| **`bank.db`** | Persistent SQLite database file storing `accounts` and `transactions` tables. |

---

## 🛠️ Requirements & Setup

### Prerequisites
- **Python 3.8+** installed on your system.
- Standard Library modules used (`sqlite3`, `sys`, `os`). No external dependencies required!

### How to Run

1. Clone or download the repository:
   ```bash
   git clone https://github.com/Jeel88/SavaliyaOne-CLI-BANK.git
   cd SavaliyaOne-CLI-BANK
   ```

2. Run the main application:
   ```bash
   python main.py
   ```

---

## 🎓 Educational Focus

This project is built to demonstrate **fundamental Python programming concepts**:
- **Modular Design**: Separation of UI (`main.py`), business logic (`account.py`), and data layer (`database.py`).
- **Database Integration**: Using SQL commands (`CREATE`, `INSERT`, `SELECT`, `UPDATE`) with Python `sqlite3`.
- **Data Persistence**: Ensuring data remains stored safely even when logging out or quitting the application.

---

## 👨‍💻 Author

**Jeel Savaliya**
- GitHub: [@Jeel88](https://github.com/Jeel88)

---

**Status:** ✅ Fully Functional & Verified
