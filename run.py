import pyfiglet
import os
import re
import time
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
SHEET = GSPREAD_CLIENT.open('Aerarium')

userdata = SHEET.worksheet('userdata')

def header():
    """
    Prints the Pyfiglet to the terminal.
    """
    print(pyfiglet.figlet_format("Aerarium"))

def subheader():
    """
    Creates a text script below the header.
    """
    print("******* A CALCULATOR FOR TODAY'S WORLD *******\n")

def fig_header():
    """
    Prints the header combination to the console.
    """
    header()
    subheader()

def thank_you():
    """
    Prints a goodbye message.
    """
    print("\n\n** THANK YOU FOR USING AERARIUM - GOODBYE! **\n")

def exit():
    """
    Clears the terminal and compiles the elements
    that make up the exit screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    thank_you()
    header()