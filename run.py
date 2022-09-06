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


def exitprog():
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
    print("This is a python-based finance tool which calculates tax-, PRSI- and USC\nliabilities. \n\nIt is based on the Irish 2021/2022 rates and presently does not account for\npension deductions, benefit-in-kind scenarios, carer's allowances etc.\n\nThis tool is meant to be used for indicative purposes only.\n")
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
            print("\033[0;32mSounds great!\033[00m\n\nLoading...\n")
            loading(1)
            clear()
            choice()
            break


def choice():
    """
    Evaluates start_choice variable and calls either salary()
    or enter() function.
    """
    if int(start_choice) == 1:
        salary()
    else:
        print(f"Thanks, {name} - let's get your data!\n")
        enter()


def name():

    """
    Asks user for a name and stores same in variable. Then calls
    the start_options() function.
    """
    while True:
        global name
        name_input = input("What is your name?\n\n")
        name = name_input.upper()
        if not re.match("^[A-Za-z-hj]*$", name):
            clear()
            print("\033[0;31mPlease try again: use letters only!\n\033[00m")
            continue
        elif name == '':
            clear()
            print("\033[0;31mPlease try again: use letters only!\n\033[00m")
            continue
        else:
            clear()
            print(f"\033[0;32mThank you, {name}!\033[00m\n")
            loading(1)
            start_options()
            break


def salary():

    """
    Asks user for salary input, validates same, creates
    variable and calls tax_credits() function.
    """
    while True:
        global salary
        salary = input(
            "What is your gross annual salary in Euros? Please round to the nearest Euro!\n\n")
        if not salary.isnumeric():
            clear()
            print(
                f"\033[0;31mSorry, {name} - {salary} is not a number. Please enter only numbers!\n\033[00m")
            continue
        else:
            clear()
            print(
                f"\033[0;32mGreat, {name}! You said your salary is {salary}€!\n\033[00m")
            loading(1)
            tax_credits()
            break


def tax_credits():

    """
    Asks user for tax credits input, validates same, creates
    variable and calls calc() function.
    """
    while True:
        global tax_credits
        tax_credits = input("What are your tax credits in Euros?\n\n")
        if not tax_credits.isnumeric():
            clear()
            print(f"\033[0;31mSorry, {name} - that is not a number. Please enter only numbers!\n\033[00m")
            continue
        else:
            clear()
            print(f"\033[0;32mGreat, {name}! You said your tax credits are {tax_credits}€!\n\033[00m")
            loading(1)
            calc()
            break


def calc():

    """
    Holder function for tax(), prsi(), usc() and summary() functions.
    Also renders mock loading messages.
    """
    clear()
    print(f"\033[0;32mMaking calculations, {name} - just a sec!\033[00m\n\nLoading.")
    loading(1)
    clear()
    print(f"\033[0;32mMaking calculations, {name} - just a sec!\033[00m\n\nLoading..")
    loading(1)
    clear()
    print(f"\033[0;32mMaking calculations, {name} - just a sec!\033[00m\n\nLoading...")
    loading(1)
    tax()
    prsi()
    usc()
    summary()


def tax():

    """
    Calculates tax based on user inputs.
    """
    global tax
    if (int(salary) * 0.2) < int(tax_credits):
        tax = 0
    elif int(salary) < 36800:
        tax = (int(salary) * 0.2) - int(tax_credits)
    else:
        tax = 7360 + ((int(salary) - 36800) * 0.4) - int(tax_credits)


def prsi():

    """
    Calculates PRSI based on user inputs.
    """
    global prsi
    if int(salary) <= 18367.36:
        prsi = 0
    elif int(salary) <= 22124.32:
        prsi = ((int(salary) * 0.04) - (626.26 - ((int(salary) - 18367.36 / 6))))
    else:
        prsi = int(salary) * 0.04


def usc():

    """
    Calculates PRSI based on user inputs.
    """
    global usc
    if int(salary) <= 13000:
        usc = 0
    elif int(salary) <= 21295:
        usc = 60.06 + (0.02 * (int(salary) - 12012))
    elif int(salary) <= 70044:
        usc = 60.06 + 185.64 + (0.045 * (int(salary) - 21296))
    else:
        usc = 60.06 + 185.64 + 2193.66 + (0.08 * (int(salary) - 70044))


def summary():

    """
    Further calculations and data interpretation.
    Outputs summary via f-string displaying all relevant sums.
    """
    clear()
    total = tax + prsi + usc
    global net
    net = int(salary) - total
    global monthly
    monthly = net / 12
    global weekly
    weekly = net / 52.18
    print(f"Summary:\n\nBased on your inputs, your tax liability is \033[0;33m{tax:.2f}€\033[00m, \nyour PRSI contributions are \033[0;33m{prsi:.2f}€\033[00m and your \nUniversal Social Charge is \033[0;33m{usc:.2f}€\033[00m.\n\nThis is a total of \033[0;33m{total:.2f}€\033[00m, leaving you with a net \nincome of \033[0;33m{net:.2f}€\033[00m per year.\n\nThis works out at a monthly wage of \033[0;33m{monthly:.2f}€\033[00m \nor a weekly wage of \033[0;33m{weekly:.2f}€\033[00m.\n")
    end()


def end():

    """
    Menu which gives user the option of saving their data
    or exiting the program.
    """
    while True:
        print("*************************************************\n")
        print("What would you like to do now?")
        print("\n1. Save your Data.")
        print("\n2. Exit the Program.")

        global end_choice
        end_choice = input("\nEnter number here: ")
        if end_choice.isalpha() or end_choice == '':
            clear()
            print(f"\n\033[0;31mSorry, {name} - that is not valid! Please enter a number between 1 and 2!\n\033[00m")
            loading(1)
            continue

        elif int(end_choice) < 1 or int(end_choice) > 2:
            clear()
            print(f"\n\033[0;31mSorry, {name} - that is not valid! Please enter a number between 1 and 2!\n\033[00m")
            loading(1)
            continue
        else:
            clear()
            loading(1)
            end_option()
            break


def pin_create():

    """
    Prompts the user to create a pin as part of the data saving process.
    Also creates a unique ID based on spreadsheet row number. Both of these
    will be displayed to the user for future reference.
    """
    clear()
    print(f"\033[0;32mGreat {name}! Let's do that!\033[00m\n\n")
    while True:
        global pin
        pin = (input("Enter a 4-digit pin number:\n\n"))
        if not pin.isnumeric() & (len(str(pin)) == 4):
            clear()
            print("\033[0;31mMust only contain 4 numbers! Try again!\n\033[00m")
            continue
        else:
            clear()
            user_data = userdata.col_values(1)
            global set_id
            set_id = len(user_data)
            print(f"\033[0;32mThank you, {name}, your unique ID is {set_id} and your pin is {pin}!\nKeep these in a safe place to access your calculation again!\033[00m\n")
            loading(1)
            break


def end_option():

    """
    Calls the pin_create() function and compiles relevant
    variable to a list which is appended to the spreadsheet as
    a new row. Then exits the program. If exit was chosen above,
    it will just call the exitprog() function without saving data.
    """
    if int(end_choice) == 1:
        pin_create()
        input("Press Enter to continue.\n")
        clear()
        data = [
            name,
            int(pin),
            int(salary),
            tax,
            prsi,
            usc,
            net,
            monthly,
            weekly,
            int(set_id)]
        print("Saving your data...\n")
        userdata.append_row(data)
        loading(1)
        print("\033[0;32mSuccess, your data has been saved! Exiting program...\033[00m\n\n")
        loading(1)
        exitprog()
    else:
        exitprog()


def enter():
    """
    Asks user to input their unique ID as part of a data
    retrieval process and validates same, before calling the
    pin_input() function.
    """
    while True:
        user_data = userdata.col_values(1)
        global set_id
        set_id = len(user_data) - 1
        global ident
        ident = input("Please enter your unique calculation ID:\n\n")
        if not ident.isnumeric() or int(ident) > set_id:
            clear()
            print(f"\033[0;31mSorry, {name} - you did not provide a valid ID number. Please enter only numbers!\n\033[00m")
            continue
        else:
            clear()
            print(f"\033[0;32mGreat, {name}! One more step and you're in...!\n\033[00m")
            pin_input()
            break


def pin_input():
    """
    Validates the users pin input against the saved pin and if
    validated calls the access_granted() function.
    """
    while True:
        global saved_pin
        saved_pin = userdata.cell((int(ident) + 1), 2).value
        global pin_input
        pin_input = input('Please enter your pin: \n')
        if not pin_input.isnumeric():
            clear()
            print(f"\033[0;31mSorry, {name} - your pin is incorrect. Please try again.\n\033[00m")
            continue
        elif not int(saved_pin) == int(pin_input):
            clear()
            print(f"\033[0;31mSorry, {name} - your pin is incorrect. Please try again.\n\033[00m")
            continue
        else:
            clear()
            loading(1)
            access_granted()
            break


def access_granted():
    """
    Returns the user's saved data from the spreadsheet row, saves the
    values into variables and then prints a summary of the user's
    data. It then gives the option to exit the program also.
    """
    values = userdata.row_values(int(ident) + 1)

    monthly_var = values[7]
    monthly_var_int = float(monthly_var)
    weekly_var = values[8]
    weekly_var_int = float(weekly_var)
    net_var = values[6]
    net_var_int = float(net_var)
    tax_var = values[3]
    tax_var_int = float(tax_var)
    prsi_var = values[4]
    prsi_var_int = float(prsi_var)
    usc_var = values[5]
    usc_var_int = float(usc_var)
    total_var_int = tax_var_int + prsi_var_int + usc_var_int
    name_var = values[0]

    print(f"Summary of {name_var}'s last calculation:\n\nBased on your inputs, your tax liability is \033[0;33m{tax_var_int:.2f}€\033[00m, your PRSI contributions are \033[0;33m{prsi_var_int:.2f}€\033[00m and your Universal Social Charge is \033[0;33m{usc_var_int:.2f}€\033[00m.\n\nThis is a total of \033[0;33m{total_var_int:.2f}€\033[00m, leaving you with a net income of \033[0;33m{net_var_int:.2f}€\033[00m per year.\n\nThis works out at a monthly wage of \033[0;33m{monthly_var_int:.2f}€\033[00m or a weekly wage of \033[0;33m{weekly_var_int:.2f}€\033[00m.\n\n")
    input("Press Enter to exit the program.\n\n")
    print("\033[0;32mExiting program...!\n\nThank you!\033[00m\n\n")
    loading(1)
    exitprog()


fig_header()
intro()
