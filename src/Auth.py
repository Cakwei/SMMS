from time import sleep
from libs.libs import clearTerminal, readAdminFile, readLecturerFile, readStudentFile, writeToStudentFile
from libs.types import TReturn, TUser
# ==========================

# Auth Functions
def login() -> TReturn:
    role: str | None = None
    # Authentication for all users
    msg = """
    [LOGIN] Select an option from below:
    1. Admin
    2. Student
    3. Lecturer

    Select an option: """
          
    username = input("[LOGIN] Enter your account name: ")
    password = input("[LOGIN] Enter your password: ")


    # Loops until one option is selected
    while True:
        role = input("\n".join(line.lstrip() for line in msg.splitlines()))
        match role.lower():
            case "1" | "2" | "3" | "Admin" | "Student" | "Lecturer":
                break
            case _:
                clearTerminal()
                print("[!] Please select from the options given")
                sleep(1.5)
                clearTerminal()
                continue

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
            
            if response["success"]:        
                return {
                    "success": True,
                    "message": "[!] Logged in succesfully",
                    "data": {
                        "username": response["data"]["username"], 
                        "name": response["data"]["name"],
                        "role": response["data"]["role"],
                        "id": response["data"]["id"]
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
                        "role": response["data"]["role"],
                        "id": response["data"]["id"]
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
                        "role": response["data"]["role"],
                        "id": response["data"]["id"]
                    }
                }

    return {
        "success": False,
        "message": "[!] An error occurred",
        "data": {}
    }

def register() -> TReturn:
    username = input("[REGISTER] Enter an account name: ")
    name = input("[REGISTER] Enter your real name: ")
    password = input("[REGISTER] Enter your password: ")

    # Check if both input is empty
    if not username or not password or not name:
        return {
            "success": False,
            "message": "[!] One or more inputs is/are empty",
            "data": {}
        }
    
    # Opens & reads the user DB, load data as dict after 
    data = readStudentFile()
    
    # Username checking if it already exists
    for d in data:
        if username.lower() == d["username"].lower():
            return {
                "success": False, 
                "message": '[!] An account with this username already exists',
                "data": {}
            } 
    
    isWriteComplete = writeToStudentFile(data, {"studentId": len(data) + 1, "username": username, "name": name, "password": password, "role": "Student"})

    if isWriteComplete:
        clearTerminal()
        print("[!] Successfully registered account")
        sleep(1.5)
        return {
            "success": True,
            "message": "",
            "data": {}
        }
    return {
        "success": False,
        "message": "[!] An error occurred",
        "data": {}
    }


# Call these only for LOGIN purposes
# For now redundant function, may need to add additional stuff later on
def getAdminCredentials(username: str, password: str) -> TReturn:
        data: list[TUser] = readAdminFile()
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
                            "role": data[i]["role"],
                            "id": data[i].get("adminId")
                        }
                    }
        return {
        "success": False,
        "message": "[!] Cannot find account or username/password is invalid!",
        "data": {}
        }


def getStudentCredentials(username: str, password: str) -> TReturn:
    data: list[TUser] =  readStudentFile()
    if len(data) >= 1:
    # For now, use linear search via username
        for i in range(len(data)):
            currentDict: TUser = data[i]
            if currentDict["username"].lower() == username.lower() and currentDict["password"] == password:
                return {
                    "success": True, 
                    "message": '[!] Successfully logged in',
                    "data": {
                        "username": data[i]["username"],
                        "name": data[i]["name"], 
                        "role": data[i]["role"],
                        "id": data[i].get("studentId") 
                    }
                }
    return {
    "success": False,
    "message": "[!] Cannot find account or username/password is invalid!",
    "data": {}
    }

def getLecturerCredentials(username: str, password: str) -> TReturn:
        data: list[TUser] = readLecturerFile()
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
                            "role": data[i]["role"],
                            "id": data[i].get("lecturerId")
                        }
                    }
        return {
        "success": False,
        "message": "[!] Cannot find account or username/password is invalid!",
        "data": {}
        }
                