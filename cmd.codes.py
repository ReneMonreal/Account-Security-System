#This is a work in progress

import random
import json
import string
# File to store the password management system data

PASSWORD_FILE = "Account_manager.json"

# Function to generate a password
def generate_password(length):
    if length < 8 :
        print("Password must be greater that atleast 9 characters!")
        return None
characters = string.ascii_letters + string.digits + "@#$%&*_-"
print(characters)

# Function to store account info in the data manager (JSON file)
def save_data_in_system(username, email, password, factorAuthenticationKeys)
    try:
        with open('Account_manager.json', 'r') as file:
            Account_manager = json.load(file)
    except:
        FileNotFoundError:
        Account_manager = {}


# Function to retrieve password by username
