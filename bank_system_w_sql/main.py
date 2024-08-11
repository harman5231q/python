from functions import create_account,check_account
from validate import user_login,register_user
from database import close_con
from bank_class import Bank




def main():
        print("--WELCOME to HARMAN's Bank--")
    #user sign in/up
        try:
            user_choice=int(input("1.Sign In As Admin \n2.Sign Up As Admin\n"  ))
            if(user_choice==1):
                user_login()

            elif(user_choice==2):
                register_user()
                main()
            else:
                print("Enter valid choice")
                main()
        except:
            print("Enter valid choice")
            main()
    #functions
        while True:
            #to make update existing acct
            print("\n1. Create New Account")
            print("2. Access Existing Account")
            print("3. Exit")
            try:
                choice = int(input("Enter your choice (1-3): "))
                if(choice==1):
                    create_account()
                elif(choice==2):
                    act=int(check_account())
                    bank=Bank(act)
                    bank.create_transaction_table()
                    while True:
                        print("\n1. Deposit Money")
                        print("2. Withdraw Money")
                        print("3. Check Balance")
                        print("4. Fund Transfer")
                        print("5. View Transaction History")
                        print("6. Go Back")

                        try:
                            sub_choice = int(input("Enter your choice (1-6): "))
                            if(sub_choice==1):
                                bank.deposit()

                            elif(sub_choice==2):
                                bank.withdraw()

                            elif(sub_choice==3):
                                bank.balance()

                            elif(sub_choice==4):
                                bank.fund_transfer()

                            elif(sub_choice==5):
                                bank.transaction_history()

                            elif(sub_choice==6):
                                break

                            else:
                                print("Enter Valid Choice")
                        except:
                            print("Enter Valid Choice")
                elif(choice==3):
                    return
            except:
                print("Enter Valid Choice")
           

if(__name__=="__main__"):
    main()
    close_con()
    