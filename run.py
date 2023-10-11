"""
Import libraries/ packages.
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


def welcome_message():
    """
    Welcome message providing the main menu of the library.
    """
    clear_tmnl()
    print("Welcome to Your Leaving Cert Library!\n")
    print("To find and check out a book, please select an option below.\n")
    print(colored(("(1) Search by Subject"), "green"))
    print(colored(("(2) Search by Publisher"), "green"))
    print(colored(("(3) Search by Book Title"), "green"))

    while True:
        welcome_answer = input("\n")
        if welcome_answer not in ("1", "2", "3"):
            print(colored(("Oops! Please choose option 1, 2 or 3"), "red"))
        else:
            break
    return welcome_answer


def search_subject(sheet_name, subject):
    """
    when user searches for book by subject
    """
    return search_google_sheet(sheet_name, 'Subject', subject)


def search_publisher(sheet_name, publisher):
    """
    when user searches for book by publisher
    """
    return search_google_sheet(sheet_name, 'Publisher', publisher)


def search_title(sheet_name, title):
    """
    when user searches for book by keyword
    """
    return search_google_sheet(sheet_name, 'Title', book_name)


def search_google_sheet(sheet_name, column_heading, search_value):
    # Open the Google Sheet by name
    try:
        sheet = client.open(sheet_name).sheet1
    except gspread.exceptions.SpreadsheetNotFound:
        return "Spreadsheet not found"
    
    # Get all values from the specified column
    column_values = sheet.col_values(sheet.find(column_heading).col)
    
    # Search for the value in the column and return matching rows
    matching_rows = [row for row in sheet.get_all_records() if row[column_heading] == search_value]
    
    return matching_rows


def clear_tmnl():
    """
    clears terminal
    """
    os.system("clear")
