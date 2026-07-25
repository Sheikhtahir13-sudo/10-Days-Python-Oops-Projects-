# BUILD BY MUHAMMAD TAHIR
# Import library
import time
from abc import ABC,abstractmethod

Customer = []       # empty lists
Account = []

class Bank(ABC):

    @abstractmethod                  # abstraction class for bank system
    def New_Customer(self):
        pass

    @abstractmethod
    def Open_account(self):
        pass

    @abstractmethod
    def Customers_info(self):
        pass

    @abstractmethod
    def Accounts_info(self):
        pass

    @abstractmethod
    def Delete_customer(self):
        pass

    @abstractmethod
    def Delete_account(self):
        pass

class customer_display(ABC):              # abstraction class for customer system

    @abstractmethod
    def Withdraw_money(self):
        pass

    @abstractmethod
    def Deposit_money(self):
        pass

    @abstractmethod
    def Transfer_money(self):
        pass

    @abstractmethod
    def Show_balance(self):
        pass

class Admin:                                      # Admin class
    def __init__(self,Username,Password):
        self.__Username = Username          # Private attributes
        self.__Password = Password

    def admin(self):
        while True:
            try:
                username = input("\nEnter username: ")
                password = input("Enter password: ")
                    
                print("\n Verification Loading... \n")
                time.sleep(3)
                    
                if username == self.__Username and password == self.__Password:            # Password verification
                    print("Login Successfully:)\n")
                    break
                    
                elif username != self.__Username and password == self.__Password:
                    print("Invalid Username try again please...\n")
                    
                elif username == self.__Username and password != self.__Password:
                    print("Invalid Password try again please...\n")
                    
                else:
                    print("Invalid Username and Password try again please...\n")
            except Exception as e:
                print(f"Error occured: {e}.\n")

class BankSystem(Bank):              # Bank system class that inherit to the bank class

    def New_Customer(self):
        while True:
            try:
                title7 = "== New customer info ==\n"
                print(title7.center(50))

                new_customer ={
                    "Customer_Id": int(input("\nEnter customer_id: ")),        # input that take data into list
                    "Name": input("Enter customer name: "),
                    "Father_name": input("Enter father name: "),
                    "Gender": input("Enter customer gender(Male/Female): "),
                    "Age": input("Enter customer age : "),
                    "Phone": input("Enter phone_no: "),
                    "Occupation": input("Enter customer occupation: "),
                    "Cnic": input("Enter cnic_no: ")
                }

                print("\n1 - Add more info")    # option for adding info
                print("2 - Just add this\n")

                choice4 = int(input("Enter choice(1-2): "))

                if choice4 == 2:
                    Customer.append(new_customer)       # add info into empty list

                    print("\n Loading... \n")
                    time.sleep(2)

                    print("\nNew customer added succesfully:)\n")   
                    break

                Customer.append(new_customer)     # add multiple customer info into list

            except Exception as e:
                print(f"Error occured: {e}.\n")
                break

    def Open_account(self):
        try:
            title8 = "== Create new account ==\n"
            print(title8.center(50))
    
            customer_id = int(input("\nEnter customer_id: "))
            status = "Active"
            Balance = int(input("Enter deposit balance: "))
            acount_no = input("Enter account number: ")
    
            if Balance <= 5000:
                pass
    
                                                                      # Customer ID check
            found = False
    
            for customer in Customer:
                if customer["Customer_Id"] == customer_id:
                    print(f"Customer_ID: {customer_id} found :)\n")   
                    found = True
                    break
    
            if not found:
                print("Customer_id not found.\n")
    
                title9 = "== First fill the new customer form ==\n"
                print(title9.center(50))
    
                return self.New_Customer()
    
                                                                 # Duplicate Account Number Check
            for account in Account:
                if account["Account_no"] == acount_no:
                    print("Account number already exists!\n")
                    return
    
            acount = {
                "Customer_ID": customer_id,
                "Account_no": acount_no,
                "Status": status,
                "Balance": Balance
            }
    
            Account.append(acount)
    
            print("\n Loading... \n")
            time.sleep(2)
    
            print("Account created successfully :)\n")
    
        except Exception as e:
            print(f"Error occured: {e}.\n")

    def Customers_info(self):
        try:
            title10 = "== Showing Customer Info ==\n"            # display customers info
            print(title10.center(50))

            print("\n Loading... \n")
            time.sleep(2)

            for i in Customer:
                print("-------------------------------------------------------------------------------------------------------------------------------------------------")
                print(i)
                print("-------------------------------------------------------------------------------------------------------------------------------------------------\n")

        except Exception as e:
            print(f"Error occured: {e}.\n")

    def Accounts_info(self):                         # display all acount info
        try:
            title11 = "== Showing Accounts Info ==\n"
            print(title11.center(50))

            print("\n Loading... \n")
            time.sleep(2)

            for i in Account:
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
                print(i)
                print("----------------------------------------------------------------------------------------------------------------------------------------------\n")

        except Exception as e:
            print(f"Error occured: {e}.\n")

    def Delete_customer(self):                            # delete specific customer info record
        try:
            title12 = "== Remove customer details =="
            print(title12.center(50))

            customer_id = int(input("Enter Customer ID: "))

            print("\n Loading... \n")
            time.sleep(2)
    
            for customer in Customer:
                if customer["Customer_Id"] == customer_id:
                    Customer.remove(customer)
                    print("Customer removed successfully :)")
                    break
            else:
                print("Customer not found.")
    
        except Exception as e:
            print(f"Error occurred: {e}.\n")

    def Delete_account(self):                                # delete specific account info record
        try:
            title13 = "== Remove account details =="
            print(title13.center(50))
            
            Account_no = input("Enter account_no: ")

            print("\n Loading... \n")
            time.sleep(2)
    
            for account in Account:
                if account["Account_no"] == Account_no:
                    Account.remove(account)
                    print("Account removed successfully :)")
                    break
            else:
                print("Account not found.")
    
        except Exception as e:
            print(f"Error occurred: {e}.\n")

class CustomerSystem(customer_display):          # Customer system class that inherit to the customer_display  class 

    def Withdraw_money(self):
        try:
            title15 = "== Withdraw Money ==\n"
            print(title15.center(50))
    
            Account_no = input("Enter account number: ")            # with drawn system that withdraw all money
    
            found = False
    
            for account in Account:
    
                if account["Account_no"] == Account_no:       # check accoount 
                    found = True
    
                    print(f"\n{account}\n")
    
                    withdraw_amount = int(input("Enter withdraw amount: "))
    
                    if withdraw_amount > account["Balance"]:
                        print("Insufficient Balance!")
                        return
    
                    account["Balance"] -= withdraw_amount

                    print("\n Loading... \n")
                    time.sleep(2)   
    
                    print(f"\nCurrent Balance: {account['Balance']}")
                    print("Money withdrawn successfully :)\n")
                    break
    
            if not found:
                print("Account not found.\n")
    
        except Exception as e:
            print(f"Error occurred: {e}.\n")

    def Deposit_money(self):
        try:
            title16 = "== Deposit Money ==\n"
            print(title16.center(50))

            Account_no = input("Enter account number: ")   # Deposit money
                
            found = False
                
            for account in Account:
                
                if account["Account_no"] == Account_no:       # check account
                    found = True
                
                    print(f"\n{account}\n")
                
                    deposit_amount = int(input("Enter deposit amount: "))

                    if deposit_amount > 0:
                        pass

                    else:
                        print("Did not deposited that amount\n")
                        return
                
                    account["Balance"] += deposit_amount

                    print("\n Loading... \n")
                    time.sleep(2)
                
                    print(f"\nCurrent Balance: {account['Balance']}")
                    print("Money deposited successfully :)\n")
                    break
                
            if not found:
                print("Account not found.\n")

        except Exception as e:
            print(f"Error occured: {e}.\n")

    def Transfer_money(self):
        try:
            title17 = "== Transfer Money ==\n"
            print(title17.center(50))
    
            account_no1 = input("Enter your account number: ")
    
            sender = None
            receiver = None    
                                                           # Find sender account
            for account in Account:
                if account["Account_no"] == account_no1:
                    sender = account
                    break
    
            if sender is None:
                print("Your account not found.\n")
                return
    
            print("\n== Your Account ==\n")
            print(sender)
    
            account_no2 = input("\nEnter receiver account number: ")    
                                                                    # Prevent transfer to same account
            if account_no1 == account_no2:
                print("You cannot transfer money to the same account.\n")
                return
                                                                   # Find receiver account
            for account in Account:
                if account["Account_no"] == account_no2:
                    receiver = account
                    break
    
            if receiver is None:
                print("Receiver account not found.\n")
                return
    
            money = int(input("Enter transfer amount: "))
    
            if money <= 0:
                print("Invalid amount.\n")
                return
    
            if money > sender["Balance"]:
                print("Insufficient Balance.\n")
                return
    
            sender["Balance"] -= money
            receiver["Balance"] += money
    
            print("\nLoading...\n")
            time.sleep(2)
    
            print("Transaction completed successfully :)")
            print(f"Your Current Balance: {sender['Balance']}\n")
    
        except Exception as e:
            print(f"Error occurred: {e}")

    def Show_balance(self):
        try:
            title18 = "== Show Balance ==\n"                # show balace of the specific account
            print(title18.center(50))

            account_no = input("Enter account number: ")
            found = False

            for account in Account:
                if account['Account_no'] == account_no:
                    found = True

                    print("\n Loading... \n")
                    time.sleep(2)
                        
                    print(f"Current Balance = {account['Balance']}")

        except Exception as e:
            print(f"Error occured: {e}.")
        
def main():                                                         # project structure
    while True:
        try:
            title1 = "===================================="
            print(title1.center(48))

            title2 = "BANK MANAGEMENT SYSTEM"
            print(title2.center(50))

            title3 = "====================================\n"
            print(title3.center(50))

            title4 = "== Admin login ==\n"
            print(title4.center(50))

            date= time.strftime("%d-%m-%Y")                     # Today date
            print(f"Today date: {date}")

            current_time = time.strftime("%H:%M:%S")                      # display current time
            print(f"Current time: {current_time}\n")

            print("1 - Admin login")
            print("2 - Exit\n")

            choice1 = int(input("Enter choice(1-2): "))

            if choice1 == 1:
                login = Admin("Tahir_17","786125")
                login.admin()

                while True:
                    title5 = "== Inventory ==\n"
                    print(title5.center(50))

                    print("1 - Bank System")                            # Bank inventory display
                    print("2 - Customer System")
                    print("3 - Exit\n")

                    choice2 = int(input("Enter choice(1-4): "))

                    if choice2 == 1:
                        bank = BankSystem()

                        while True:
                            title6 = "== Bank Categories ==\n"            # Bank categories display
                            print(title6.center(50))

                            print("1 - New customer")
                            print("2 - Open account")
                            print("3 - Customers Details")
                            print("4 - Accounts Details")
                            print("5 - Delete customer records")
                            print("6 - Delete account records")
                            print("7 - Exit\n")

                            choice3 = int(input("Enter choice(1-4): "))

                            if choice3 == 1:
                                bank.New_Customer()

                            elif choice3 == 2:
                                bank.Open_account()

                            elif choice3 == 3:
                                bank.Customers_info()

                            elif choice3 == 4:
                                bank.Accounts_info()

                            elif choice3 == 5:
                                bank.Delete_customer()

                            elif choice3 == 6:
                                bank.Delete_account()

                            elif choice3 == 7:
                                print("\nThanks for using the bank system:)\n")
                                break

                            else:
                                print("Invalid option\n")
                                break

                    elif choice2 == 2:
                        customer = CustomerSystem()

                        while True:
                            title14 = "== Customers Categories ==\n"           # Customer categories display
                            print(title14.center(50))

                            print("1 - Withdraw Money")
                            print("2 - Deposit Money")
                            print("3 - Transfer Money")
                            print("4 - Show Balance")
                            print("5 - Exit\n")

                            choice5 = int(input("Enter choice(1-5): "))

                            if choice5 == 1:
                                customer.Withdraw_money()

                            elif choice5 == 2:
                                customer.Deposit_money()

                            elif choice5 == 3:
                                customer.Transfer_money()

                            elif choice5 == 4:
                                customer.Show_balance()

                            elif choice5 == 5:
                                print("Thanks for using the customer system:)\n")
                                break

                            else:
                                print("Invalid option\n")
                                break

                    elif choice2 == 3:
                        print("Thanks for using this program:)\n")
                        break

                    else:
                        print("Invalid option\n")
                        break

            elif choice1 == 2:
                print("Thanks for using this program:)\n")
                break

            else:
                print("Invalid option\n")
                break

        except Exception as e:
            print(f"Error occured: {e}.\n")

if __name__ == "__main__":   # main engine
    main()