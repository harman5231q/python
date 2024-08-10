class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ₹{amount}")
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")
        return self.balance

    def view_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions found.")

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000  # Starting account number

    def create_account(self, account_holder):
        account_number = self.next_account_number
        self.next_account_number += 1
        self.accounts[account_number] = BankAccount(account_number, account_holder)
        print(f"Account created successfully for {account_holder}.")
        print(f"Your account number is {account_number}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

def main():
    bank_system = BankSystem()

    while True:
        print("\n1. Create New Account")
        print("2. Access Existing Account")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            account_holder = input("Enter the account holder's name: ")
            bank_system.create_account(account_holder)

        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            account = bank_system.get_account(account_number)

            if account:
                while True:
                    print("\n1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. View Transaction History")
                    print("5. Go Back")

                    sub_choice = input("Enter your choice (1-5): ")

                    if sub_choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif sub_choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif sub_choice == "3":
                        account.check_balance()
                    elif sub_choice == "4":
                        account.view_transaction_history()
                    elif sub_choice == "5":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Account not found.")

        elif choice == "3":
            print("Thank you for using the Banking System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
