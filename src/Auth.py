import json
import sys
from pathlib import Path

# ==========================
# Resolve import issues from another parent folder
current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent

# Add the root directory to Python's search path
sys.path.append(str(root_dir))

from libs.types import TReturn, TAdmins
# ==========================

# Auth Functions
def login() -> TReturn:
    # Authentication for all users
    username = input("[LOGIN] Enter your account name: ")
    password = input("[LOGIN] Enter your password: ")

    # Check if both input is empty
    if not username or not password:
        return {
            "success": False,
            "message": "[!] One or more inputs is/are empty",
            "data": {}
        }

    # ================
    # Variable section
    # ================
    data: list[TAdmins] = []
    # ================

    # Opens the user DB and load data as dict 
    with open('./db/admins.json', 'r') as file:
        data = json.load(file)


    if len(data) >= 1:
        # For now, use linear search via username
        for i in range(len(data)):
            currentDict = data[i]
            if currentDict["username"].lower() == username.lower() and currentDict["password"] == password:
                return {
                    "success": True, 
                    "message": 'Logged in',
                    "data": {
                        "username": data[i]["username"],
                        "role": data[i]["role"]
                    }
                }
          
          
    return {
        "success": False,
        "message": "[!] Account with this username is not found!",
        "data": {}
    }

def register():
    username = input("[REGISTER] Enter an account name: ")
    password = input("[REGISTER] Enter your password: ")

    # Check if both input is empty
    if not username or not password:
        return {
            "success": False,
            "message": "[!] One or more inputs is/are empty",
            "data": {}
        }

    # Opens the user DB and load data as dict 
    with open('./db/students.json', 'r') as file:
        data: list[TAdmins] = json.load(file)
        print(type(data))
        exit()


