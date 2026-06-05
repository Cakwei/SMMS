import json
from lib.types import TAdmins, TReturn

def login() -> TReturn:
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
    data: list[TAdmins] = []
    # ================

    # Opens the user DB and load data as dict 
    with open('admins.json', 'r') as file:
        data = json.load(file)


    if len(data) >= 1:
        # For now, use linear search via username
        for i in range(len(data)):
            if data[i]["username"] == username and data[i]["password"] == password:
                return {"success": True, "message": 'Logged in'}
          
          
    return {
        "success": False,
        "message": "[!] Account with this username is not found!"
    }

def register():
    pass

print(login()['success'])