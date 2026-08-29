# BUILD BY MUHAMMAD TAHIR
# Import Library
import time
from abc import ABC,abstractmethod

Customer = [
    {
        "Customer_ID": 101,     # Usrs info and pin 
        "Name": "Tahir",
        "Pin": 7864,
        "Balance": 50000
    },
    {
        "Customer_ID": 102,
        "Name": "Moiz",
        "Pin": 1254,
        "Balance": 1000000
    }
]

class ATM(ABC):                             # abstract methods of all menu functions

    @abstractmethod
    def New_Account(self):
        pass

    @abstractmethod
    def Deposit_Money(self):
        pass

    @abstractmethod
    def Withdraw_Money(self):
        pass

    @abstractmethod
    def Show_Balance(self):
        pass

class ATMSystem(ATM):
    def New_Account(self):                                    # New account system
        try:
            title2 = "== New Account ==\n"
            print(title2.center(50))
    
            customer = {
                "Customer_ID":int(input("Enter customer id: ")),      # customer data
                "Name":input("Enter name: "),
                "Pin":int(input("Enter pin: ")),
                "Balance":int(input("Enter deposit balance: "))
            }
    
            found = False
    
            customer_id = int(input("Enter customer id again: "))
    
            for user in Customer:
                if user["Customer_ID"] == customer_id:               # customer id validation
                    found = True
                    print("\nCustomer_ID already existed.\n")
                    break
    
            if not found:
                Customer.append(customer)                           # add all info into list 
                print("\nNew account added succesfully:)\n")

        except Exception as e:
            print(f"Error occured: {e}.\n")

    def Deposit_Money(self):
        try: 
            title3 = "== Deposit Money ==\n"               # Deposit system
            print(title3.center(50))

            found = False
        
            pin = int(input("Enter your pin: "))

            for customer in Customer:
    
                if customer["Pin"] == pin:                    # pin verification

                    found = True
    
                    print("\nCorrect PIN :)\n")
                    print("-------------------------------------------------------------------------")
                    print(customer)
                    print("-------------------------------------------------------------------------\n")

                    amount = int(input("Enter deposit amount: "))

                    if amount <= 0:
                        print("Invalid amount.\n")

                    else:
                        customer["Balance"] += amount                        # Money add into balance
                        print("\nMoney Deposited Successfully :)")

                        print("Loading...\n")
                        time.sleep(2)

                        print(f"Deposit Amount : {amount}\n")                    # deposit money amount
            if not found:
                print("Invalid pin\n")
                return
            
        except Exception as e:
            print(f"Error occured: {e}.\n")

    def Withdraw_Money(self):                                  # Withdraw system
        try: 
            title4 = "== Withdraw Money ==\n"
            print(title4.center(50))

            found = False

            pin = int(input("Enter your pin: "))
            
            for customer in Customer:
    
                if customer["Pin"] == pin:                             # pin verification

                    found = True
    
                    print("\nCorrect PIN :)\n")
                    print("-------------------------------------------------------------------------")
                    print(customer)
                    print("-------------------------------------------------------------------------\n")

                    amount = int(input("Enter withdrawn amount: "))

                    if amount <= 0:
                        print("Invalid amount.\n")

                    else:
                        customer["Balance"] -= amount                      # money subtract into balance
                        print("\nMoney Withdrawn Successfully :)")

                        print("Loading...\n")
                        time.sleep(2)

                        print(f"Withdrawn Amount : {amount}\n")                 # withdraw money amount           
            if not found:
                print("Invalid pin\n")
                return

        except Exception as e:
            print(f"Error occured: {e}.\n")

    def Show_Balance(self):
        try:
            title5 = "== Show Balance ==\n"                        # Balance system
            print(title5.center(50))

            found = False

            pin = int(input("Enter your pin: "))

            for customer in Customer:
                
                if customer["Pin"] == pin:                      # pin verification

                    found = True
                
                    print("\nCorrect PIN :)\n")

                    time.sleep(2)
                    print(f"Current Balance = {customer['Balance']}\n")          # show total balance

            if not found:
                print("Invalid pin\n")
                return

        except Exception as e:
            print(f"Error occured: {e}.\n")
                    
def main():
    while True:                                             # main System
        try:
            print("=" * 45)
            print("ATM SYSTEM".center(45))
            print(f"{"=" * 45}\n")

            date = time.strftime("%d-%m-%Y")
            current_time = time.strftime("%H:%M:%S")          # display date

            print(f"Date : {date}")
            print(f"Time : {current_time}\n")                     # display time

            print("1 - ATM System")
            print("2 - Exit\n")

            choice1 = int(input("Enter choice (1-2): "))

            if choice1 == 1:

                atm = ATMSystem()
                while True:    
                    title1 = "==  Menu ==\n"                          # system categories
                    print(title1.center(50))

                    print("1 - New account")
                    print("2 - Deposit money")
                    print("3 - Withdraw money")
                    print("4 - Show balance")
                    print("5 - Exit\n")

                    choice2 = int(input("Enter choice(1-2): "))

                    if choice2 == 1:
                        atm.New_Account()

                    elif choice2 == 2:
                        atm.Deposit_Money()                          # calling out of all functions

                    elif choice2 == 3:
                        atm.Withdraw_Money()

                    elif choice2 == 4:
                        atm.Show_Balance()

                    elif choice2 == 5:
                        print("Thanks fr using ATM System:)\n")
                        break

                    else:
                        print("Invalid option\n")
                        break

            elif choice1 == 2:
                print("\nThank you for using this program :)")
                break

            else:
                print("Invalid Choice.\n")

        except Exception as e:
            print(f"Error occured: {e}.\n")
            break

if __name__ == "__main__":           # main engine
    main()
