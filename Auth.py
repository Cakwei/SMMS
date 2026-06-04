import json

def login():
    # Authentication for all users
    username = input("Enter your account name: ")
    password = input("Enter your password: ")

    # Check if both input is empty
    if not username or not password:
        return {
            "success": False,
            "message": "[!] One or more inputs is/are empty" 
        }

    # ================
    # Variable section
    # ================
    data: None | dict = None 
    # ================

    # Opens the user DB and load data as dict 
    with open('users.json', 'r') as file:
        data = json.load(file)

    # For now, use linear search via userId


    return {
        'username': username,
        'password': password
    }

def register():
    pass

print(login())