from customer import *
from database import *
def create_account():
    name=input("Enter customer's Name : ")
    address=input("Enter Address of customer : ")
    cust = Customer(name,address)
    cust.createuser()

def check_account():
    try:
        act=int(input("Enter Account Number : "))
        temp=db_query(f"SELECT Account_number FROM customers where Account_number='{act}'")
        if temp:
            return act
        else:
            print("No Such Account Number Exists")
            check_account()
    except:
        print("Enter Valid Account Number")
