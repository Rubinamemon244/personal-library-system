# Library Management System           

book_list = list()

# menu items
menu = """Library Management System
1. Add Book
2. Remove Book
3. View Books
4. Press E to Exit
"""

# add books
def add_book(booklist, book):
    booklist.append(book)
    print("Book added successfully.")

# remove books
def remove_book(booklist, book):
    if book in booklist:
        booklist.remove(book)
        print("Book removed successfully.")
    else:
        print("Book not found in the list.")

# display all books
def display_list(booklist):
    if booklist:
        print("Added Books ->", ", ".join(booklist))
    else:
        print("No books in the list.")

# exit program
def exit_program():
    print("Jazak Allah for visiting the book library system. Goodbye!")
    quit()

# ✅ Main program loop (outside of any function)
while True:
    print(menu)
    choice = input("Enter your choice: ")

    if choice == "1":  # add book
        book_name = input("Enter the book name you want to add: ")
        add_book(book_list, book_name)

    elif choice == "2":  # remove book
        book_name = input("Enter the book name you want to remove: ")
        remove_book(book_list, book_name)

    elif choice == "3":  # view books
        display_list(book_list)

    elif choice.lower() == "e":  # exit program
        exit_program()

    else:
        print("Invalid choice. Please choose a valid option.")
        input("Press Enter to continue...")
