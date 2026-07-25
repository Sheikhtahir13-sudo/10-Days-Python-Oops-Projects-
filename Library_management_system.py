# BUILD BY MUHAMMAD TAHIR
# Import library
import time
from abc import ABC,abstractmethod

Customer_info = []          # Empty lists
sells = []

Books = [                        # 5 Books data already store in list
    {
        "Book_ID": 101,
        "Title": "Python",
        "Author": "Ali",
        "Category": "Programming",
        "Price": 1400,
        "Quantity": 10
    },
    {
        "Book_ID": 102,
        "Title": "Java",
        "Author": "Ahmed",
        "Category": "Programming",
        "Price": 1500,
        "Quantity": 13
    },
    {
        "Book_ID": 101,
        "Title": "Python Programming",
        "Author": "John Zelle",
        "Category": "Programming",
        "Price": 1800,
        "Quantity": 15
    },
    {
        "Book_ID": 102,
        "Title": "Data Structures",
        "Author": "Mark Allen Weiss",
        "Category": "Computer Science",
        "Price": 2200,
        "Quantity": 8
    },
    {
        "Book_ID": 103,
        "Title": "Machine Learning Basics",
        "Author": "Aurélien Géron",
        "Category": "Artificial Intelligence",
        "Price": 3500,
        "Quantity": 9
    }
]

class Library(ABC):             # Abstraction ABC inherit with library parent class

    @abstractmethod
    def Add_Books(self):                        # abstract method used for all system categories 
        pass

    @abstractmethod
    def remove_book(self):              
        pass

    @abstractmethod
    def display_books(self):
        pass

    @abstractmethod
    def buy_book(self):
        pass

    @abstractmethod
    def sells(self):
        pass

    @abstractmethod
    def customer_info():
        pass

class Admin():
    def __init__(self,Username,Password):          # class for admin login

        self.__Username = Username          # Encapsulation used for make private attribute
        self.__Password = Password

    def show(self):                          
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
                print(f"Error occured: {e}.")

class librarySystem(Library):    # inherit to the parent class

    def Add_Books(self):                              # New books function
            while True:
                try:
                    title3 = "== ADD Books =="
                    print(title3.center(50))
    
                    
                    new_book = {
                        "Book_ID": int(input("\nEnter Book_id: ")),             # Take input to store in the list
                        "Title": input("Enter Title:"),
                        "Auther": input("Enter Auther: "),
                        "Category": input("Enter Category: "),
                        "Price": int(input("Enter Price: ")),
                        "Quantity": int(input("Enter Quantity:"))
                    }
    
                    print("\n1 - Add more books")      # Add more books permission
                    print("2 - Just add\n")
    
                    choice3 = int(input("Enter choice(1-2): "))
    
                    print("\n Loading... \n")
                    time.sleep(3)
    
                    if choice3 == 2:
                        Books.append(new_book)                # Append in the list
                        print("Book added succesfully:)")
                        break
    
                except Exception as e:
                    print(f"Error occured: {e}.")

    def display_books(self):  # Display all books that store in books list
        try:
            title4 = "== Display all books ==\n"
            print(title4.center(50))
    
            print("\n Loading... \n")
            time.sleep(3)
    
            for i in Books:     # loop for print all book info
                print("------------------------------------------------------------------------------------------------------------------------------")
                print(i)
                print("------------------------------------------------------------------------------------------------------------------------------\n")
                
        except Exception as e:
            print(f"Error occured: {e}.")

    def remove_book(self):      
        try:
            title5 = "== Delete books record ==\n"
            print(title5.center(50))
    
            book_id = int(input("\nEnter book id: "))
    
            print("\n Loading... \n")
            time.sleep(3)
    
            for book in Books:
                if book["Book_ID"] == book_id:           # Remove specific book info
                    Books.remove(book)
                    print("Book deleted succesfully:)\n")
                    break
            else:
                print("Book not found")
        except Exception as e:
                print(f"Error occured: {e}.")

    def buy_book(self):
        while True:
            try:
                title6 = "== Purchase books ==\n"
                print(title6.center(50))
    
                purchase = {
                    "Buyer_Name": input("Enter Buyer Name: "),      # input to store in the list
                    "Phone": input("Enter Phone Number: "),
                    "Book_title": input("Enter Book Title: ")
                }
    
                Customer_info.append(purchase)      # append in the list
    
                book1 = input("Enter book title agin: ")
    
                print("\n Loading... \n")
                time.sleep(3)
    
                for book in Books:
                    if book["Title"] == book1:    # loop to check book list index
    
                        if book["Quantity"] > 0:
                            book["Quantity"] -= 1
                            sells.append(book["Price"])
    
                            print("------------------------------------------")     # Customer info
                            print(book)
                            date1 = time.strftime("%d-%m-%Y")
                            print(f"\nToday date = {date1}")
                            print("\nBook purchased successfully :)")
                            print("------------------------------------------\n")
                        else:
                            print("Book is out of stock!")
                        return
    
                print("Book not found")
                return
    
            except Exception as e:
                print(f"Error occurred: {e}")

    def sells(self):
        try:
            title7 = "== Selling amount ==\n"
            print(title7.center(50))

            print("\n Loading... \n")
            time.sleep(2)
        
            Total = sum(sells)         # sum of all book amount that sells today
            print(f"Total selling amount = {Total}\n")
    
        except Exception as e:
            print(f"Error occured: {e}.")

    def customer_info(self):
        try:
            title8 = "== Customer info ==\n"
            print(title8.center(50))

            print("\n Loading... \n")
            time.sleep(2)
    
            for i in Customer_info:         # loop show the customer info 
                print("--------------------------------------------------------------------------------")
                print(i)
                print("--------------------------------------------------------------------------------\n")
    
        except Exception as e:
            print(f"Error occured: {e}.")
            
def main():               
    while True:
        try:
            title1 = "===================================="
            print(title1.center(48))

            title2 = "LIBRARY MANAGEMENT SYSTEM"
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
                admin = Admin("Tahir_17","786125")
                admin.show()

                while True:
                    title3 = "== Categories ==\n"
                    print(title3.center(50))

                    print("1 - Add new books record")       # options
                    print("2 - Display all books")
                    print("3 - Delete books record")
                    print("4 - Purchase books")
                    print("5 - View total amount")
                    print("6 - Customer info")
                    print("7 - Logout\n")

                    choice2 = int(input("Enter choice(1-6): "))
                                                                        # if-else condition
                    if choice2 == 1:
                        c1 = librarySystem()
                        c1.Add_Books()

                    elif choice2 == 2:
                        c2 = librarySystem()
                        c2.display_books()

                    elif choice2 == 3:
                        c3 = librarySystem()
                        c3.remove_book()

                    elif choice2 == 4:
                        c4 = librarySystem()
                        c4.buy_book()

                    elif choice2 == 5:
                        c5 = librarySystem()
                        c5.sells()

                    elif choice2 == 6:
                        c6 = librarySystem()
                        c6.customer_info()

                    elif choice2 == 7:
                        print("Thanks for using this program:)\n")
                        break
        except Exception as e:
            print(f"Error occured: {e}.")
            break
                    
main()                    # main engine
