"""
Import libraries/ packages.
"""
import os
import sys
from termcolor import colored
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('book_repository')


def load_books():
    """
    Load all books in the spreadsheet.
    """
    global numberOfBooks
    clear_screen()
    print("Please wait while books are being loaded...")
    print("Done loading books.\n")

    booklist = SHEET.worksheet('books')
    data = booklist.get_all_values()

    # Extract the data rows
    all_data = data[1:]
    # total number of books
    numberOfBooks = len(all_data)

    # Create dictionaries for easy access
    book_info = {}
    for row in all_data:
        title, publisher, subject = row
        book_info[title] = {'publisher': publisher, 'subject': subject}

    return book_info


def search_books_by_field(books, search_field, search_term):
    """
    Search for books by a specific field (title, publisher, subject).
    """
    matching_books = {}
    for title, info in books.items():
        if search_term.lower() in info[search_field].lower():
            matching_books[title] = info

    return matching_books


def checkout_message(book_title):
    clear_screen()
    print(f"Great! You have successfully checked out '{book_title}'.")
    print("Please collect it from the library reception by 3pm today.")
    print("Enjoy your reading!")


def main():
    """
    Start the program and runs until user exits
    """
    books = load_books()
    running = True
    
    
    while True:
        clear_screen()
        print("Welcome to Your Leaving Cert Library!")
        print(f"There are currently {len(books)} books in the library.")
        print("To find and check out a book, please select an option below:")
        print("(1) Search by Subject")
        print("(2) Search by Publisher")
        print("(3) Search by Title")

        user_choice = input("Enter your choice (1/2/3): ")

        if user_choice == "1":
            search_term = input("Please enter the subject: ")
            matching_books = search_books_by_field(books, 'subject', search_term)
        elif user_choice == "2":
            search_term = input("Please enter the publisher: ")
            matching_books = search_books_by_field(books, 'publisher', search_term)
        elif user_choice == "3":
            search_term = input("Please enter the title: ")
            matching_books = search_books_by_field(books, 'title', search_term)
        else:
            print("Oops! Please choose option 1, 2, or 3.")
            continue

        if not matching_books:
            print(f'Sorry, no matching books found for "{search_term}".')

        for title in matching_books:
            print(f'Title: {title}, Publisher: {matching_books[title]["publisher"]}, Subject: {matching_books[title]["subject"]}')

        book_to_checkout = input("Enter the title of the book you want to check out (or 'q' to quit): ")
        
        if book_to_checkout.lower() == 'q':
            break

        if book_to_checkout in matching_books:
            checkout_book(book_to_checkout)
        else:
            print("Book not found in the search results. Please try again.")


def loop():
    # Welcome the user to the program
    welcome_answer = welcome_message()

    # Select the books you want to print
    if welcome_answer == ("1"):  # Search by subject
        print("Please enter Subject below:")
        searchword = input("\n")  # Use input
        print("")
        print(f"Search term is '{searchword}'")
        # search_subject()
    elif welcome_answer == ("2"):  # Search by publisher
        print("Please enter Publisher below:")
        searchword = input("\n")  # Use input
        print("")
        print(f"Search term is '{searchword}'")
        # search_publisher()"""
    elif welcome_answer == ("3"):  # Search by title
        print("Please enter Title below:")
        searchword = input("\n")  # Use input
        print("")
        print(f"Search term is '{searchword}'")
        search_results = search_by_title(searchword)
        print(search_results)


def clear_screen():
    """
    Clear the terminal screen.
    """
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


main()
