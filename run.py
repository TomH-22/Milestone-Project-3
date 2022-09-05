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

def loading(seconds):
    """
    Makes the program pause for x seconds.
    """
    time.sleep(seconds)

def intro():
    """
    Prints info about the program and calls the
    name() function.
    """
    print("This is a python-based finance tool which calculates tax-, PRSI- and USC liabilities. \n\nIt is based on the Irish 2021/2022 rates and presently does not account for pension deductions, benefit-in-kind scenarios, carer's allowances etc.\n\nThis tool is meant to be used for indicative purposes only.\n")
    name()

def clear():
    """
    Clears the terminal and compiles a new header.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    fig_header()

def start_options():
    """
    Displays initial action menu to user and compiles
    start_choice to variable.
    """
    while True:
        print("What would you like to do?")
        print("\n1. Make a new calculation.")
        print("\n2. Retrieve a saved calculation.")

        global start_choice
        start_choice = input("\nEnter number here: ")
        if start_choice.isalpha() or start_choice == '':
            clear()
            print(f"\n\033[0;31mSorry, {name} - that is not valid! Please enter a number between 1 and 2!\n\033[00m")
            loading(1)
            continue

        elif int(start_choice) < 1 or int(start_choice) > 2:
            clear()
            print(f"\n\033[0;31mSorry, {name} - that is not valid! Please enter a number between 1 and 2!\n\033[00m")
            loading(1)
            continue
        else:
            clear()
            print(f"\033[0;32mSounds great!\033[00m\n\nLoading...\n")
            loading(1)
            clear()
            choice()
            break

