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
    clear_tmnl()
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

    if welcome_answer == ("1"):
        print("Please enter Subject:")
        search_subject()
    elif welcome_answer == ("2"):
        print("Please enter Publisher:")
        search_publisher()
    elif welcome_answer == ("3"):
        print("Please enter Title:")
        search_title()


# Find the column index under the heading
header_row = SHEET.row_values(1)
column_index = header_row.index() + 1  # Add 1 because gspread uses 1-based indexing

# Get all the values under the heading
# Now, 'values' contains all the data under the specified heading
values = SHEET.col_values(column_index)

# Heading variables to call
title = header_row.column_index(1)
subject = header_row.column_index(2)
publisher = header_row.column_index(3)


def search_subject(SHEET, subject):
    """
    when user searches for book by subject
    """
    if input == "":
        return search_repository(SHEET, 'Subject', subject)
    else exception gspread.exceptions.CellNotFound
    print("Sorry could not find that in the library!")


def search_publisher(SHEET, publisher):
    """
    when user searches for book by publisher
    """
    if input == "":
        return search_repository(SHEET, 'Publisher', publisher)
    else exception gspread.exceptions.CellNotFound
    print("Sorry could not find that in the library!")


def search_title(SHEET, title):
    """
    when user searches for book by keyword
    """
    if input == "":
        return search_repository(SHEET, 'Title', title)
    else exception gspread.exceptions.CellNotFound
    print("Sorry could not find that in the library!")


def search_repository():
    

def clear_tmnl():
    """
    clears terminal
    """
    os.system("clear")
