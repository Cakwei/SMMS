import json
from time import sleep
from libs.types import TClasses, TResults, TReturn, TSessionData, TUser 

def getMOTD(sessionData: TSessionData | dict):   
    role = sessionData["role"] if len(sessionData) >= 1 else None
    txt = "Welcome to Student Marks Management System"
    borderLength = len(txt) + 4
    topBorder = "*" * borderLength
 
    # Dynamically read the current state of 'role'
    sessionTxt = f" SESSION: {role.upper() if role else None} "
    bottom_border = sessionTxt.center(borderLength, "*")
    programName = f"{topBorder}\n* {txt} *\n{bottom_border if role else topBorder}"
    return programName, topBorder

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

def readClassesFile() -> list[TClasses]:
    with open('./db/class.json', 'r') as file:
        data: list[TClasses] = json.load(file)
    return data

# Param :-
# Username = Find results from that username
def getOwnResults(sessionData: TSessionData | dict) -> TReturn:
  
    # Related to data in results.json
    filteredResultsData: list[TResults] = []
    resultsData: list[TResults] = readResultsFile()

    # Related to data in classes.json
    classesData: list[TClasses] = readClassesFile()

    while True:
        programName, topBorder = getMOTD(sessionData)
        motdMsg = f"""{programName}
            \033[4mFetch my results from...\033[0m

            1. Fetch specific semester
            2. Fetch all semester
            {topBorder}\n"""
        
        print("\n".join(line.lstrip() for line in motdMsg.splitlines()))
        option = input("")

        match option.lower():
            case "1" | "fetch all" | "all":
                filteredResultsData = []

                # Map classId to its details for instant O(1) lookups
                classesMap = {c["classId"]: c for c in classesData}
                # print("classesMap @ libs.py", classesMap)
                
                # Filter and merge the data
                for result in resultsData:
                    if result.get("studentId") == sessionData["id"]:
                        # Get the corresponding class details using the classId
                        classInfo = classesMap.get(result["classId"], {})
                        
                        # Create a combined dictionary
                        combinedResult: TResults = {
                            "resultId": result["resultId"],
                            "classId": result["classId"],
                            "className": classInfo.get("className"),
                            "semester": classInfo.get("semester"),
                            "score": result["score"]
                        }
                        filteredResultsData.append(combinedResult)

                return {
                    "success": True,
                    "message": "[!] Successfully fetched user's own results",
                    "data": {
                        "resultsData": filteredResultsData
                    }
                }

            case "2" | "fetch specific" | "specific":
                break

            case _:
                clearTerminal()
                print("[!] Please select a valid option")
                sleep(1.5)
                clearTerminal()

    # Check if results file is empty or not
    if len(resultsData) <= 0:
        return {
            "success": False,
            "message": "[!] No results found in database.",
            "data": {}
        }

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

# AI-generated function (I can't do IDE UI stuff)
def printResult(resultData: list):
    if not resultData:
        print("\n" + "="*50)
        print("   No results found for this student.   ")
        print("="*50 + "\n")
        return

    # Header UI
    print("\n" + "═" * 65)
    print(f"║ {'STUDENT ACADEMIC PERFORMANCE DASHBOARD'.center(61)} ║")
    print("═" * 65)
    
    # Table Column Headers
    # Format layout: ID (6), Class Name (22), Semester (10), Score (8)
    print(f" │ {'ID':<4} │ {'Class Name':<20} │ {'Semester':<8} │ {'Score':<6} │")
    print(" ├" + "─"*6 + "┼" + "─"*22 + "┼" + "─"*10 + "┼" + "─"*8 + "┤")

    total_score = 0
    
    # Loop through and print rows
    for row in resultData:
        r_id = row.get("resultId", "-")
        c_name = row.get("className", "Unknown")
        sem = f"Sem {row.get('semester', '-')}"
        score = row.get("score", 0)
        
        total_score += score
        
        # Truncate class name if it's too long for the column layout
        if len(c_name) > 20:
            c_name = c_name[:17] + "..."
            
        print(f" │ {r_id:<4} │ {c_name:<20} │ {sem:<8} │ {score:<6} │")

    # Footer UI & Summary Stats
    print(" └" + "─"*6 + "┴" + "─"*22 + "┴" + "─"*10 + "┴" + "─"*8 + "┘")
    
    # Calculate Average
    avg_score = total_score / len(resultData)
    
    print("─" * 65)
    print(f"  Total Classes: {len(resultData):<15} Average Score: {avg_score:.2f}%")
    print("═" * 65 + "\n")