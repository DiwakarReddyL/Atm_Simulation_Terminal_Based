import mysql.connector
# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="Add Your MySql user name",     
        password="Add Your MySql Password", 
        database="atm_simulation"
    )

# Register new user
def register_user():
    conn = connect_db()
    cursor = conn.cursor()
    print("\n=== Register New Account ===")
    account_number = int(input("Enter a new Account Number: "))
    name = input("Enter your name: ")
    pin = int(input("Set your 4-digit PIN: "))

    # Check if account already exists
    cursor.execute("SELECT * FROM accounts WHERE account_number = %s", (account_number,))
    if cursor.fetchone():
        print(" Account already exists! Try logging in.")
    else:
        cursor.execute(
            "INSERT INTO accounts (account_number, name, pin, balance) VALUES (%s, %s, %s, 1000.00)",
            (account_number, name, pin)
        )
        conn.commit()
        print(" Account registered successfully with ₹1000 initial balance.")

    conn.close()

# Login user
def login_user():
    conn = connect_db()
    cursor = conn.cursor()
    print("\n=== User Login ===")
    account_number = int(input("Enter your Account Number: "))
    pin = int(input("Enter your PIN: "))

    cursor.execute("SELECT * FROM accounts WHERE account_number = %s AND pin = %s", (account_number, pin))
    account = cursor.fetchone()
    conn.close()
    return account

# Deposit
def deposit(account_number, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, account_number))
    conn.commit()
    conn.close()
    print("Amount deposited successfully.")

# Withdraw
def withdraw(account_number, amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
    current_balance = cursor.fetchone()[0]

    if amount <= current_balance:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s", (amount, account_number))
        conn.commit()
        print(f"₹{amount} withdrawn successfully.")
    else:
        print("Insufficient balance.")
    conn.close()

# Check Balance
def check_balance(account_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
    balance = cursor.fetchone()[0]
    conn.close()
    print(f" Current Balance: ₹{balance}/-")

# Change PIN
def change_pin(account_number):
    conn = connect_db()
    cursor = conn.cursor()
    current_pin = int(input("Enter current PIN: "))
    cursor.execute("SELECT pin FROM accounts WHERE account_number = %s", (account_number,))
    db_pin = cursor.fetchone()[0]

    if current_pin == db_pin:
        new_pin = int(input("Enter new PIN: "))
        cursor.execute("UPDATE accounts SET pin = %s WHERE account_number = %s", (new_pin, account_number))
        conn.commit()
        print(" PIN updated successfully.")
    else:
        print(" Incorrect current PIN.")
    conn.close()

# Main ATM system
def atm_system():
    while True:
        print("\n======= Welcome to ATM =======")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Select option: ")

        if option == "1":
            register_user()

        elif option == "2":
            user = login_user()
            if user:
                account_number = user[0]
                print(f"\n Welcome back, {user[1]}!")

                while True:
                    print("\n--- ATM Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Balance Inquiry")
                    print("4. Change PIN")
                    print("5. Logout")

                    choice = input("Choose option: ")

                    if choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        if amount > 0:
                            deposit(account_number, amount)
                        else:
                            print(" Invalid amount.")

                    elif choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        if amount > 0:
                            withdraw(account_number, amount)
                        else:
                            print(" Invalid amount.")

                    elif choice == "3":
                        check_balance(account_number)

                    elif choice == "4":
                        change_pin(account_number)

                    elif choice == "5":
                        print(" Logged out.")
                        break

                    else:
                        print(" Invalid option.")

            else:
                print(" Login failed. Check account number or PIN.")

        elif option == "3":
            print(" Thank you for using the ATM.")
            break

        else:
            print(" Invalid option.")
# Start the ATM system
atm_system()
