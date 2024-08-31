# Banking System

This Banking System is a Python-based application that uses MySQL for database management. The system is designed to manage bank accounts, allowing users to perform various banking operations such as creating accounts, managing customers, and performing transactions.

## Project Structure

The project consists of the following key files:

- **`bank_class.py`**: Contains the main `Bank` class, which manages the overall banking operations and interactions with the database.
- **`customer.py`**: Defines the `Customer` class, handling individual customer details and operations.
- **`database.py`**: Manages the database connection and provides functions to interact with the MySQL database.
- **`functions.py`**: Contains utility functions used across the application, including validation and data manipulation.
- **`main.py`**: The entry point of the application, where the main logic and user interface are handled.
- **`validate.py`**: Includes functions for validating user inputs to ensure data integrity.

## Features

### 1. Account Management

- **Create Account**: Allows users to create new bank accounts by providing necessary details like name, address, and initial deposit.
- **Edit Account**: Enables editing of existing account details.
- **Delete Account**: Allows for the deletion of an account from the system.

### 2. Customer Management

- **Add Customer**: Add new customers to the bank.
- **View Customer Details**: Retrieve and display information about existing customers.
- **Edit Customer Details**: Update customer information as needed.

### 3. Transaction Management

- **Deposit Money**: Deposit funds into an account.
- **Withdraw Money**: Withdraw funds from an account.
- **Transfer Funds**: Transfer money between accounts.
- **Check Balance**: View the current balance of an account.

### 4. Database Management

- **MySQL Integration**: The system uses MySQL for storing and managing all the data related to accounts, customers, and transactions.
- **Secure Data Handling**: Ensures that all sensitive data is securely managed and stored in the database.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**
- **MySQL**: A running instance of MySQL to store the banking data.
- **Required Python Libraries**: Install the required Python libraries by running:
  ```bash
 pip install mysql-connector-python
