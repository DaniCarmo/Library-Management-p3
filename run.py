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

# Error handling if json file not found
try:
    CREDS = Credentials.from_service_account_file('creds.json')
except FileNotFoundError as e:
    print(f"Error: 'creds.json' file not found. Make sure the file exists.")

SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('book_repository')


def clear_screen():
    """
    Clear screen for better UX design
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def load_books():
    """
    Load all books in the spreadsheet.
    """
    print("Please wait while books are being loaded...")

    # Handle error if spreadsheet cannot load
    try:
        booklist = SHEET.worksheet('books')
        data = booklist.get_all_values()
    except gspread.exceptions.APIError as e:
        print(f"An error occurred while accessing Google Sheets: {e}")
        print("Please come back later and try again!")

    # Extract data rows
    all_data = data[1:]

    # Create dictionaries of results
    book_info = {}
    for row in all_data:
        title, publisher, subject = row
        book_info[title] = {
            'title': title,
            'publisher': publisher,
            'subject': subject
            }

    print("Ok let's go!\n")
    return book_info


def search_by_field(books, search_field, search_term):
    """
    Search for books by specific field (title, publisher, subject).
    """
    matching_books = {}
    for title, info in books.items():
        if search_term.lower() in info[search_field].lower():
            matching_books[title] = info

    return matching_books


def checkout_message(book_title):
    """
    Message to appear to user upon checking out
    """
    print(f"Great! You have successfully checked out '{book_title}'\n")
    print("Please collect from the library reception by 3pm today.\n")
    print("Enjoy your reading!\n")
    # Add horizontal line
    print("-" * 50)
    print("Back to main menu:")


def checkout_book(books, matching_books):
    """
    User confirmation to checkout or quit when/if book found
    """
    while True:
        checkout_choice = input("Enter book title to checkout or "
                                "'m' for main menu:\n")

        if checkout_choice.strip().lower() == 'm':
            return  # Return to the main menu

        if checkout_choice.strip() in matching_books:
            book_title = checkout_choice.strip()
            print(colored((f"You selected: '{book_title}'\n"), "green"))
            confirm = input("Confirm checkout (y/n): \n").strip().lower()
            if confirm == 'y':
                clear_screen()
                checkout_message(book_title)
                break
            else:
                print("Ok let's try that again!\n")
        else:
            print(colored(("Looks like our library does not "
                           "have that book.\n"), "red"))
            print(colored(("Let's see if we can help find what you're "
                           "looking for!\n"), "green"))


def handle_user_choice():
    """
    Enter search term and bring user to checkout once confirmed
    """
    clear_screen()
    search_term = ""
    matching_books = {}
    if user_choice == "1":
        search_term = input("Please enter the subject: \n")
        clear_screen()
        matching_books = search_by_field(books, 'subject', search_term)
    elif user_choice == "2":
        search_term = input("Please enter the publisher: \n")
        clear_screen()
        matching_books = search_by_field(books, 'publisher', search_term)
    elif user_choice == "3":
        search_term = input("Please enter the title: \n")
        clear_screen()
        matching_books = search_by_field(books, 'title', search_term)
    else:
        print_menu()
        print(colored(("Oops! Please choose option 1, 2, or 3."), "red"))
        return

    for title in matching_books:
        print(f'Title: {title}')
        print(f'Publisher: {matching_books[title]["publisher"]}')
        print(f'Subject: {matching_books[title]["subject"]}\n')

    if not matching_books:
        print(f'Uh oh! No matching books found for "{search_term}".\n')
        print("Let's give it another shot.")
    else:
        checkout_book(books, matching_books)


def print_menu():
    """
    Menu search options
    """
    print("To find and check out a book, please select an option below:\n")
    print(colored(("(1) Search by Subject"), "green"))
    print(colored(("(2) Search by Publisher"), "green"))
    print(colored(("(3) Search by Title"), "green"))
    print(colored("(4) Quit", "red"))


def main():
    """
    Display the main menu and get user choice
    """
    clear_screen()
    print("Welcome to Your Leaving Cert Library!\n")

    global books
    books = load_books()

    while True:
        print_menu()
        global user_choice
        user_choice = input("Enter your choice (1/2/3/4): \n")

        if not user_choice:
            print(colored("Please enter an option above to continue", "red"))
        elif user_choice == "4":
            print("Goodbye! Thanks for using the library system.")
            break
        else:
            handle_user_choice()


if __name__ == "__main__":
    main()
