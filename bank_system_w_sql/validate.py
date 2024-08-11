from database import *

def user_login():
        username=input("Enter Your Username : ")
        temp = db_query(f"SELECT username FROM admin WHERE username='{username}';")
        # print(temp)
        if temp:
            for i in range (5):
                password=input("Enter password : ")
                temp1=db_query(f"SELECT password from admin where username ='{username}'")
                if(temp1[0][0]==password):
                    print(f"\nYou Are logged in as {username.capitalize()}.\n")
                    break
                else:
                    print("Try again!")
                    
        else:
            print("Please enter valid Username")
            user_login()

def register_user():
    username=input("Enter Username You Want : ")
    temp = db_query(f"SELECT username FROM admin WHERE username='{username}';")
    if temp:
        print("Username Already taken Try Another One")
        register_user()
    else:
        print(f"{username.capitalize()} Username Available")
        password=input("Enter password : ")
        db_query(f"INSERT INTO admin (username, password) VALUES ('{username}', '{password}');")
        my_db.commit()

        print(f"{username.capitalize()} is Succesfully Registered as Admin")

