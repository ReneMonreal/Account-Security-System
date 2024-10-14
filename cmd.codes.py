import string
import random
import json


"""
Last Updated - 10/14/2024 - Rene Monreal
Todo: Start on Login Feautre
Check if i can create two accounts with the same username, this should null
"""


# Basic Info: Storage 
Account_File = "Account_Manager.json"
characters = string.punctuation + string.digits + string.ascii_letters
print("running")

def generate_password(length):  # Code to generate Password
    # Checks for a valid password length
    if length < 8:
        print("Invalid: Password Must be Atleast 8 Characters Long: ")
        return
    elif length > 32:
        print("Invalid: Password Must be Less Than 32 Characters Loong: ")
        return
    while True:  # Once true, generate random password
        password = "".join(random.choice(characters) for _ in range(length))
        # Checks to see if it contains these character types (at least one)
        if (any(c.isalpha() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password
        else: #IMPORTANT, this will prevent the username from getting sent to the JSON file if the password is invalid
            print("Password Generated did not meet requiremments ")
            continue

def save_account_credentials(username, password):#Fuction to store the username and paswords into the JSON file
    try:
        with open(Account_File, "r") as file:
            password_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        #If the account file is not found start with zero
        password_data = {}
    password_data[username] = password

    with open(Account_File, "w") as file:
        json.dump(password_data, file)
        file.flush()
    
def load_accounts():#Loads all existing accounts in the Json file, NOTE: Check for time & space o(n**2)
    try:
        with open(Account_File, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return empty dict if file not found or invalid

# Main Point
print(" ")
print("Hello... Welcome to my Account Management Software")
print("Login = 1")
print("Create an account = 2")
print("Quit = 3")

while True:
    action = int(input("What would you like to do ? "))
    if action == 2:  # User wants to create an account
        print("*********")
        accounts_in_database = load_accounts() 
        username = input("What will be your username? ")
        if username in accounts_in_database:  # If username is in the Database (JSON file), then print it is taken.
            print("Username is taken, Please select another username: ")
            continue  # Instead of 'return', use 'continue' to prompt again
        # Asks if user wants to enter a custom password or create a new one
        print("Custom Password = 2")
        print("Random Password = 3")
        password_action = int(input("What will you like to do today? "))
        if password_action == 2:  # User wants a custom password
            print("*******")
            print("NOTE: Password must include a special character, a number, and a letter:")
            password = input("What do you want your password to be? ")
            if len(password) < 8:
                print("Password must be at least 8 characters long: ")
                continue
            elif len(password) > 32:
                print("Password must be less than 32 characters long: ")
                continue
            else:
                if (any(c.isalpha() for c in password) and
                    any(c.isdigit() for c in password) and
                    any(c in string.punctuation for c in password)):
                    print("Account Created Succsesfully!!!")
                    save_account_credentials(username, password)
                    break  # End the account creation process after successful password creation
                else: #IMPORTANT, this will prevent the username from getting sent to the JSON file if the password is invalid
                    print("Password does not meet requirenments")
                    continue
        elif password_action == 3:  # User wants to generate a random password:
            length = int(input("Enter your desired password length: "))
            password = generate_password(length)
            if password: #If password is returned/ valid from Genrate_passwrod function
                save_account_credentials(username, password)
                break
            else:
                print("Password Genreation failed, please try again")
                continue
    elif action == 1:  # User wants to log in
    # requesting username and password
        login_username = input("What is your username? ")
        login_password = input("What is your password")
    if login_username in accounts and accounts[login_username] == login_password:
        print(f"Access Granted, welcome {login_username}")
    else:
        print("Username or password does not match or is incorrect")
        break  # End the loop if login fails
