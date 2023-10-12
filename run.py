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


def welcome_message():
    """
    Welcome message providing the main menu of the library
    """
    clear_screen()
    print("Welcome to Your Leaving Cert Library!\n")
    print(f"There are currently {numberOfBooks} books in the library.\n")
    print("To find and check out a book, please select an option below:\n")
    print(colored(("(1) Search by Subject"), "green"))
    print(colored(("(2) Search by Publisher"), "green"))
    print(colored(("(3) Search by Title"), "green"))

    while True:
        welcome_answer = input("\n")
        if welcome_answer not in ("1", "2", "3"):
            print(colored(("Oops! Please choose option 1, 2 or 3"), "red"))
        else:
            break
    return welcome_answer


def load_book_repository():
    """
    Load all books in the spreadsheet.
    """
    global all_titles, all_publishers, all_data, all_subjects, numberOfBooks
    clear_screen()
    print("Please wait while books are being loaded...")
    print("Done loading books.\n")

    booklist = SHEET.worksheet('books')
    data = booklist.get_all_values()

    # Extract the header and data rows
    headerSpreadsheet = data[0]
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


def check_out(book_title):
    clear_screen()
    while True:
        user_choice = input(f"Would you like to check out '{book_title}'?")
        print("Type 'yes' or 'no'): ")
        if user_choice.lower() == 'yes':
            print(f"Great you have successfully checked out '{book_title}'.\n")
            print("Please collect from the library reception by 3pm today.\n")
            print("Enjoy your reading!")
            break
        elif user_choice.lower() == 'no':
            print("Ok then let's help you find what you're looking for.\n")
            print("Returning to search menu...")
            break
        else:
            print("Oops! Invalid input.\n")
            print("Type 'yes' to check out book or 'no' to search again.")


def main():
    """
    Start the program and runs other functions continuously until
    the user exits
    """
    load_book_repository()
    running = True

    """"
    Runs the following functions continuously unless you quit it.
    """

    while True:
        if not running:
            break
        loop()
        # running = return_to_begin(running)


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
