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
    print(colored(("(3) Search by Keyword"), "green"))

    while True:
        welcome_answer = input("\n")
        if welcome_answer not in ("1", "2", "3"):
            print(colored(("Oops! Please choose option 1, 2 or 3"), "red"))
        else:
            break
    return welcome_answer
