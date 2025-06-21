#  ATM Simulation Project
This is a simple Python project that simulates basic ATM functionalities using a MySQL database. It allows users to create an account, log in, deposit and withdraw money, check their balance, and change their PIN.
---
## Features
- Register a new user with account number and PIN
- Login with account number and PIN
- Deposit amount to account
- Withdraw amount with balance validation
- Balance inquiry
- Change account PIN
- Logout
---
## Technologies Used
- Python
- MySQL
---
## Database Setup
Before running the project, make sure MySQL is installed and running. Then execute the following SQL commands:

```sql
CREATE DATABASE atm_simulation;

USE atm_simulation;

CREATE TABLE accounts (
    account_number VORCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    pin INT,
    balance FLOAT DEFAULT 1000.00
);
```

## Install this package
```
pip install mysql-connector-python
```
---
## Update the MySQL connection credentials in the Python code
---
- host="localhost"
- user="root"
- password="your_mysql_password"
- database="atm_simulation"
---
## Run the Python script
```
python atm_simulation.py
```
