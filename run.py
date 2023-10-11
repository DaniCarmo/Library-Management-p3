"""
Import libraries and packages.
"""
import os
import sys
import random
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


"""
Variables for worksheet.
"""
LIST_ALL = SHEET.worksheet('books')


def welcome_message():
    """
    Welcome message for user
    """
    clear_terminal()
    print("Welcome to your Leaving Cert Library!\n")
    print("Please chose from an option below:\n")
    print(colored(("1. View All Books"), "green"))
    print(colored(("2. Chose at Random"), "green"))
    print(colored(("3. Search for Book"), "green"))

    while True:
        if welcome_answer not in ("1", "2", "3"):
            print(colored(("Invalid input. Please try again."), "red"))
            print(colored(("Please choose an option between 1 and 3."), "red"))
        else:
            break
    return welcome_answer


def load_books():
    """
    List all books in the spreadsheet.
    """
    global headerSpreadsheet, numberOfBooks, numberOfColumns, \
        title, author, illustrator, interest_level, \
        reading_age, reading_stage, synopsis
    clear_terminal()
    print("Please wait while books are being loaded...")

    all_books = SHEET.worksheet('main_list')
    headerSpreadsheet = all_books.row_values(1)
    numberOfBooks = len(all_books.col_values(1))-1
    numberOfColumns = len(all_books.row_values(1))

    all_rows = []
    for ind in range(1, numberOfBooks):
        all_col = all_books.col_values(ind)
        all_rows.append(all_col[1:])
    title = all_rows[0]
    author = all_rows[1]
    """
    To get the author, you can choose all the columns,
    including the header in row 1.
    To remove the first row in Python,
    we need to start counting at 0 instead of 1,
    and then remove row 0 according to that count.
    """
    illustrator = all_rows[2]
    interest_level = all_rows[3]
    reading_age = all_rows[4]
    reading_stage = all_rows[5]
    synopsis = all_rows[6]

    print("Done loading books.")


def print_book_list(index_print_list):
    """
    The print_book_list function displays book titles
    and authors by using a list of indices as input.
    It shows the book titles on top,
    and displays a message when there are no results to show.
    """
    clear_terminal()
    print('\n Book Title(s):\n')
    if len(index_print_list) > 0:
        for ind in index_print_list:
            print(f"{title[ind]} - {author[ind]}")
    else:
        print("no results found")


def random_book_message():
    """
    This feature lets users pick a book at random from one of four categories:
    early childhood, middle childhood, late childhood, and adolescence.
    """
    clear_terminal()
    print("The Random Book Picker, \n")
    print("Chooses a book at random from the selected category, \n")
    print("Taking into account the child's\n")
    print("expected mental and developmental age. \n")
    print("Please select a category:\n")
    print(colored(("(1) Early Childhood 0-5 years old"), "green"))
    print(colored(("(2) Middle Childhood 6-8 years old"), "green"))
    print(colored(("(3) Late Childhood 9-11 years old"), "green"))
    print(colored(("(4) Adolescence 12-15 years old"), "green"))
    print(colored(("(5) Any category"), "green"))

    while True:
        random_book_picker_ans = input("\n")
        if random_book_picker_ans not in ("1", "2", "3", "4", "5"):
            print(colored(("Invalid input."), "red"))
            print(colored(("Please try again."), "red"))
        else:
            break
        print(colored(("Choose from the options listed:"), "red"))
        print(colored(("Option 1 to 5."), "red"))

    return random_book_picker_ans


def search_string_within_info(search_string, information_to_search_from):
    """
    This function looks for a specific word
    or phrase in a list of data
    and gives you a list of where it was found.
    """
    index_print_list = []
    for index in range(len(information_to_search_from)):
        if search_string in information_to_search_from[index]:
            index_print_list.append(index)
    return index_print_list


def random_from_index_list(index_list):
    """
    This function requires a list of indices as input.
    It will randomly select one of the indices and return it inside a new list.
    """
    random_number = random.choice(index_list)
    random_number = [random_number]
    return random_number


def clear_terminal():
    """
    Clears the terminal when called.
    """
    # (Credited in README.md to Tony118g)
    os.system("clear")


def return_to_begin(running):
    """
    The `return_to_begin` function shows a message
    with choices to go back to the main menu or exit the program.
    After that, it waits for the user to type either `0` to go back to
    the main menu or `x` to exit the program.
    """
    print(colored(("(0) Return to main menu"), "green"))
    print(colored(("(x) Quit program"), "red"))

    while True:
        main_list_ans = input("\n")
        if main_list_ans not in ("0", "x"):
            print(colored(("Invalid input."), "red"))
            print(colored(("Please try again."), "red"))
        else:
            break
        print(colored(("Choose 0 to return to the main"), "red"))
        print(colored(("or x to quit."), "red"))

    if main_list_ans == ("0"):
        return running
    if main_list_ans == ("x"):
        running = False
        return running


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
    """
    This function is the main loop of the application.
    It welcomes the user and prompts them to select
    an option from the main menu.
    Depending on the user's selection,
    it either prints a complete list of books,
    selects a random book from a specific category,
    or allows the user to search for books by entering a search term.
    It then prints the selected books to the console.
    """
    # Welcome the user to the program
    welcome_answer = welcome_message()

    # Select the books you want to print
    if welcome_answer == ("1"):  # List all books
        index_print_list = range(numberOfBooks)

    elif welcome_answer == ("2"):  # Random book picker
        random_book_picker_ans = random_book_message()
        if random_book_picker_ans == ("0"):
            welcome_message()
        elif random_book_picker_ans == ("1"):
            searchword = "early childhood"
        elif random_book_picker_ans == ("2"):
            searchword = "middle childhood"
        elif random_book_picker_ans == ("3"):
            searchword = "late childhood"
        elif random_book_picker_ans == ("4"):
            searchword = "adolescence"
        elif random_book_picker_ans == ("5"):
            searchword = ""

        index_print_list = search_string_within_info(searchword, reading_stage)
        print(index_print_list)
        index_print_list = random_from_index_list(index_print_list)

    elif welcome_answer == ("3"):  # Search for a term in title and author
        print("Type your search term below:")
        searchword = input("\n")  # Use input
        print("")
        print(f"Search term is '{searchword}'")
        index_print_list_title = search_string_within_info(searchword, title)
        index_print_list_author = search_string_within_info(searchword, author)
        index_print_list = index_print_list_title + index_print_list_author

    # Selection is made, print all relevant books
    print_book_list(index_print_list)


main()