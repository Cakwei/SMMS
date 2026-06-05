import json
import sys
from pathlib import Path
from time import sleep

# ==========================
# Resolve import issues from another parent folder
current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent

# Add the root directory to Python's search path
sys.path.append(str(root_dir))

from libs.types import TReturn, TUser
# ==========================

# Auth Functions
def login() -> TReturn:
    # Authentication for all users
    msg = """
    [LOGIN] Select an option from below:
    1. Admin
    2. Student
    3. Lecturer

    Select an option: """
          
    username = input("[LOGIN] Enter your account name: ")
    password = input("[LOGIN] Enter your password: ")
    role = input("\n".join(line.lstrip() for line in msg.splitlines()))

    # Check if both input is empty
    if not username or not password or not role:
        return {
            "success": False,
            "message": "[!] One or more inputs is/are empty",
            "data": {}
        }

    # ================
    # Variable section
    # ================
    # data: list[TAdmins] = []
    # ================

    match role.lower():
        case "1" | "admin":  
            # Opens the admin DB and load data as dict
            response: TReturn = getAdminCredentials(username, password)
            print(response["data"]["username"], 'peirgjearpgokfijkgaeornlfnkalgeosrkjlgaern')
            if response["success"]:        
                return {
                    "success": True,
                    "message": "[!] Logged in succesfully",
                    "data": {
                        "username": response["data"]["username"], 
                        "name": response["data"]["name"],
                        "role": response["data"]["role"]
                    }
                }
            
        case "student" | "2":
            # Opens the student DB and load data as dict
            response: TReturn = getStudentCredentials(username, password)

            if response["success"]:        
                return {
                    "success": True,
                    "message": "[!] Logged in succesfully",
                    "data": {
                        "username": response["data"]["username"],     
                        "name": response["data"]["name"],
                        "role": response["data"]["role"]
                  
                    }
                }
            

        case "lecturer" | "3":
            # Opens the admin DB and load data as dict
            response: TReturn = getLecturerCredentials(username, password)

            if response["success"]:        
                return {
                    "success": True,
                    "message": "[!] Logged in succesfully",
                    "data": {
                        "username": response["data"]["username"], 
                        "name": response["data"]["name"],
                        "role": response["data"]["role"]
                    }
                }
            

    return {
        "success": False,
        "message": "[!] An error occurred",
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
        data: list[TUser] = json.load(file)
        print(type(data))
        exit()

# For now redundant function, may need to add additional stuff later on
def getAdminCredentials(username: str, password: str) -> TReturn:
    with open('./db/admins.json', 'r') as file:
        data: list[TUser] = json.load(file)
        if len(data) >= 1:
            # For now, use linear search via username
            for i in range(len(data)):
                currentDict: TUser = data[i]
                if currentDict["username"].lower() == username.lower() and currentDict["password"] == password:
                    return {
                        "success": True, 
                        "message": 'Logged in',
                        "data": {
                            "username": data[i]["username"],
                            "name": data[i]["name"], 
                            "role": data[i]["role"]
                        }
                    }
        return {
        "success": False,
        "message": "[!] Cannot find account or username/password is invalid!",
        "data": {}
        }


def getStudentCredentials(username: str, password: str) -> TReturn:
    with open('./db/students.json', 'r') as file:
        data: list[TUser] = json.load(file)
        if len(data) >= 1:
            # For now, use linear search via username
            for i in range(len(data)):
                currentDict: TUser = data[i]
                if currentDict["username"].lower() == username.lower() and currentDict["password"] == password:
                    return {
                        "success": True, 
                        "message": 'Logged in',
                        "data": {
                            "username": data[i]["username"],
                            "name": data[i]["name"], 
                            "role": data[i]["role"]
                        }
                    }
        return {
        "success": False,
        "message": "[!] Cannot find account or username/password is invalid!",
        "data": {}
        }

def getLecturerCredentials(username: str, password: str) -> TReturn:
    with open('./db/lecturers.json', 'r') as file:
        data: list[TUser] = json.load(file)
        if len(data) >= 1:
            # For now, use linear search via username
            for i in range(len(data)):
                currentDict: TUser = data[i]
                if currentDict["username"].lower() == username.lower() and currentDict["password"] == password:
                    return {
                        "success": True, 
                        "message": 'Logged in',
                        "data": {
                            "username": data[i]["username"],
                            "name": data[i]["name"], 
                            "role": data[i]["role"]
                        }
                    }
        return {
        "success": False,
        "message": "[!] Cannot find account or username/password is invalid!",
        "data": {}
        }
                