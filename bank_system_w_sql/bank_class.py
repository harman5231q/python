from database import *
import datetime
from functions import *

class Bank:
    def __init__(self,  account_number):
        self.__account_number = account_number
        self.create_transaction_table()

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__account_number}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"remarks VARCHAR(50),"
                 f"amount INTEGER );")
    

    def balance(self):
        temp = db_query(
            f"SELECT balance FROM customers WHERE Account_number = '{self.__account_number}';")
        print(f"Balance of Account Number {self.__account_number} is ₹{temp[0][0]}")
    

    def deposit(self):
        try:
            funds=int(input("Enter Total Amount to be deposited : "))
            temp = db_query(
            f"SELECT BALANCE FROM customers WHERE Account_number = '{self.__account_number}';")
            # print(temp[0][0])
            test = temp[0][0] + funds
            db_query(
            f"UPDATE customers SET balance = '{test}' WHERE Account_number = '{self.__account_number}'; ")
            my_db.commit()
            db_query(f"INSERT INTO {self.__account_number}_transaction (timedate,remarks,amount) VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'Amount Deposit',"
                 f"'{funds}'"
                 f");")
            self.balance()
        except:
            print("Enter Valid funds")
    

    def withdraw(self):
        try:
            amount=int(input("Enter Total Amount to be withdrawn : "))
            temp = db_query(
                f"SELECT BALANCE FROM customers WHERE Account_number = '{self.__account_number}';")
            if amount > temp[0][0]:
                print("Insufficient Balance Please Deposit Money")
            else:
                test = temp[0][0] - amount
                db_query(
                    f"UPDATE customers SET balance = '{test}' WHERE Account_Number = '{self.__account_number}'; ")
                my_db.commit()
                self.balance()
                db_query(f"INSERT INTO {self.__account_number}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f");")
        except:
            print("Enter Valid funds")


    def fund_transfer(self):
        print("Enter the Account details to which fund to be transfered.")
        to_account=check_account()
        act=Bank(to_account)
        try:
            amount=int(input("Enter Total Amount to be transfered : "))
            temp = db_query(
                f"SELECT BALANCE FROM customers WHERE Account_number = '{self.__account_number}';")
            if amount > temp[0][0]:
                print("Insufficient Balance Please Deposit Money")
            else:
                test = temp[0][0] - amount

                temp1 = db_query(
                f"SELECT BALANCE FROM customers WHERE Account_number = '{to_account}';")

                # print(temp[0][0])
                test1 = temp1[0][0] + amount
                db_query(
                    f"UPDATE customers SET balance = {test} WHERE Account_Number = '{self.__account_number}'; ")
                # my_db.commit()
                db_query(
                f"UPDATE customers SET balance = {test1} WHERE Account_number = '{to_account}'; ")
                my_db.commit()

                db_query(f"INSERT INTO {to_account}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'Fund Transfer From {self.__account_number}',"
                         f"'{amount}'"
                         f");")
                db_query(f"INSERT INTO {self.__account_number}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'Fund Transfer -> {to_account}',"
                         f"'{amount}'"
                         f");")
                act.balance()
                self.balance()
        except:
            print("Enter Valid funds")


    def transaction_history(self):
        temp=db_query(f"SELECT * FROM {self.__account_number}_transaction;")
        print(temp)