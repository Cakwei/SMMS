import json
from time import sleep
from libs.types import TResults, TReturn, TSessionData, TUser 

def clearTerminal():
    print("\033[H\033[J", end="")

def readResultsFile() -> list[TResults]:
    with open('./db/results.json', 'r') as file:
        data: list[TResults] = json.load(file)
    return data

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

# Param :-
# Username = Find results from that username
def getOwnResults(sessionData: TSessionData | dict) -> TReturn:
    filteredData: list[TResults] = []
    data: list[TResults] = readResultsFile()

    # Check if results file is empty or not
    if len(data) <= 0:
        return {
            "success": False,
            "message": "[!] No results found in database.",
            "data": {}
        }
    
    # Filter results array to only show own results  
    for d in data:
        # If studentId equals to id of logged in user, then continue 
        # For now, use linear search via username
        if d.get("studentId") == sessionData["id"]:
            filteredData.append(d)

    if len(filteredData) >= 1:
        print(filteredData)
        while True:
            option = input("Do you want go back? (Yes/No): ")
            match option.lower():
                case "yes":
                    break
                case _:
                    continue

    return {
        "success": False,
        "message": "[!] User with this username does not exist.",
        "data": {}
    }
    
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
