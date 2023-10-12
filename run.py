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
    # clear_tmnl()
    print("Welcome to Your Leaving Cert Library!\n")
    print("To find and check out a book, please select an option below.\n")
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
    List all books in the spreadsheet.
    """
    global all_titles, all_publishers, all_data
    clear_tmnl()
    print("Please wait while books are being loaded...")

    booklist = SHEET.worksheet('books')
    data = booklist.get_all_values()

    # Extract the header and data rows
    headerSpreadsheet = data[0]
    all_data = data[1:]

    numberOfBooks = len(all_data)
    numberOfColumns = len(headerSpreadsheet)
    print("number of books = ")
    print(numberOfBooks)
    print("number of cols = ")
    print(numberOfColumns)

    # Create lists to store titles, publishers and subjects
    all_titles = [row[0] for row in all_data]
    all_publishers = [row[1] for row in all_data]
    all_subjects = [row[2] for row in all_data]

    # Print the titles and publishers
    print("all_titles = ")
    print(all_titles)
    print("all_publishers = ")
    print(all_publishers)
    print("all_subjects = ")
    print(all_subjects)

    print("Done loading books.")


def search_by_title(title_to_search):
    """
    This function looks for a specific wo
    rd
    or phrase in a list of data
    and gives you a list of where it was found.
    """
    for i, title in enumerate(all_titles):
        if title == title_to_search:
            return all_data[i]
    return None  # Return None if the title is not found


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
    """if welcome_answer == ("1"):  # Search by subject
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
    if welcome_answer == ("3"):  # Search by title
        print("Please enter Title below:")
        searchword = input("\n")  # Use input
        print("")
        print(f"Search term is '{searchword}'")
        search_results = search_by_title(searchword)
        print(search_results)


def clear_tmnl():
    """
    clears terminal
    """
    os.system("clear")


main()
