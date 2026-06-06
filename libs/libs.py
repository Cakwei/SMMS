import json
from libs.types import TUser 

def clearTerminal():
    print("\033[H\033[J", end="")

def readStudentFile() -> list[TUser]:
    with open('./db/students.json', 'r') as file:
        data: list[TUser] = json.load(file)
    return data

def readLecturerFile() -> list[TUser]:
    with open('./db/lecturers.json', 'r') as file:
        data: list[TUser] = json.load(file)
    return data

def readAdminFile() -> list[TUser]:
    with open('./db/admins.json', 'r') as file:
        data: list[TUser] = json.load(file)
    return data

def writeToStudentFile(data: list[TUser], newData: TUser) -> bool:
    try:
        data.append(newData)

        with open("./db/students.json", "w") as file:
            json.dump(data, file, indent=4)
        return True
    
    except FileNotFoundError:
        print("Error: The specified file could not be found.")
        return False

    except PermissionError:
        print("Error: You do not have permission to access this file.")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False