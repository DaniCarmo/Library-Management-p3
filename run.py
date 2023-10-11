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

booklist = SHEET.worksheet('books')


def welcome_message():
    """
    Welcome message providing the main menu of the library
    """
    # clear_tmnl()
    print("Welcome to Your Leaving Cert Library!\n")
    print("To find and check out a book, please select an option below.\n")
    print(colored(("(1) Search by Subject"), "green"))
    print(colored(("(2) Search by Publisher"), "green"))
    print(colored(("(3) Search by Title"), "green"))

    while True:
        if welcome_answer not in ("1", "2", "3"):
            print(colored(("Oops! Please choose option 1, 2 or 3"), "red"))
        else:
            break
    return welcome_answer


def main():
    """
    The `main()` function starts the program,
    loads books, and runs other functions continuously until
    the user exits using the `return_to_begin()` function.
    """
    load_books()
    running = True

    """"
    Runs the following functions continuously unless you quit it.
    """

    while True:
        if not running:
            break
        loop()
        running = return_to_begin(running)


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
        # search_publisher()
    elif welcome_answer == ("3"):  # Search by title
        print("Please enter Title below:")
        searchword = input("\n")  # Use input
        print("")
        print(f"Search term is '{searchword}'")
        # search_title()

# Find the column index under the heading
header_row = booklist.row_values(1)
# Add 1 because gspread uses 1-based indexing
column_index = header_row.index() + 1

# Get all the values under the heading
# Now, 'values' contains all the data under the specified heading
values = booklist.col_values(column_index)

# Heading variables to call

# title = header_row.column_index(1)
# subject = header_row.column_index(2)
# publisher = header_row.column_index(3)


def clear_tmnl():
    """
    clears terminal
    """
    os.system("clear")


main()
