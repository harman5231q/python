from database import *
import random
class Customer:

    def __init__(self, name,address,):

        self.__name = name
        self.__address = address
        self.__accounts=0
        

    def createuser(self):
        while True:

            self.__accounts=random.randint(0,100000)
            temp=db_query(f"SELECT Account_number FROM customers where Account_number='{self.__accounts}'")
            if temp:
                continue
            else:
                db_query(f"INSERT INTO customers (Account_number,NAME,ADDRESS,BALANCE,STATUS) VALUES ('{self.__accounts}', '{self.__name}',  '{self.__address}', '500' ,  1  );")
                my_db.commit()
                break

        print(f"Account Succesfully Created for {self.__name}.\nYour Account Number is {self.__accounts}")



# b=Customer("harman","12025")sdnkj
# b.createuser()