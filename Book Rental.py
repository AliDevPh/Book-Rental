print("="*40)
print("      WELCOME TO BOOK RENTAL\n     Borrow any books for free")
print("="*40)

available_books = ("\n1: Lord of the rings\n2: The Loud House")

def books(display_books=True):
    if display_books:
        print("1. Lord of the Rings")
        print("2. The Loud House")

def loop():
    while True:
        print("\nPress 1: Show Available Books")
        print("Press 2: Borrow Book")
        print("Press 3: Return Book")
        print("Press 4: Exit")

        try:
            enter = int(input("\nEnter your Choice: "))
        except ValueError:
            print("Invalid Input")
            continue  

        if enter == 1:
            print("\n -- Available Books -- ", available_books)
        elif enter == 2:
            books()
            print("\nThis is a one-time borrowing of book")
            borrow_book = int(input("What book do you want to borrow?: "))
            
            if borrow_book == 1:
                print("\nReleased: Lord of the Rings\n")
            elif borrow_book == 2:
                print("\nReleased: The Loud House\n")
        elif enter == 3:
            books()
            return_book = int(input("What book are you returning?: "))
            
            if return_book == 1:
                print("\nReturned: Lord of the Rings\n")
            elif return_book == 2:
                print("\nReturned: The Loud House\n")
        elif enter == 4:
            print("Exiting the program.")
            return False  
        else:
            print("Invalid Choice. Please try again.")
            
        return True  

should_continue = True
while should_continue:
    should_continue = loop()
