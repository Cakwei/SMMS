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
#        
            case "2" | "fetch specific" | "specific":
                filteredResultsData = []
                highestSemester = 0

                # Map classId to its details for instant O(1) lookups
                classesMap = {c["classId"]: c for c in classesData}
                
                # Filter and merge the data
                for result in resultsData:
                    print(result)
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

                # Loops thru filteredResults data and append to set, duplicates will be removed, then get the largest num
                highestSemester: int = max({(d.get("semester") or 0) for d in filteredResultsData})

                while True:
                    option = int(input(f"Select your current/past enrolled semester to view your results [1 - {highestSemester}]: "))
                    if not isinstance(option, int):
                        clearTerminal()
                        print("[!] Please select a number")
                        sleep(1.5)
                        clearTerminal()
                    else: break

                # A variable to store filtered results by specific semester
                filteredResultsDataBySemester = []
                for d in filteredResultsData:
                    currentDataSemester:int  = d.get("semester") or 0
                    if currentDataSemester == int(option):
                        filteredResultsDataBySemester.append(d)

                print(filteredResultsDataBySemester)
                return {
                    "success": True,
                    "message": "[!] Successfully fetched user's own results",
                    "data": {
                        "resultsData": filteredResultsDataBySemester
                    }
                }

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
def printResult(resultsData: list):
    if not resultsData:
        print("\n" + "="*50)
        print("   No results found for this student.   ")
        print("="*50 + "\n")
        return

    # 1. Dynamically calculate the maximum width needed for the Class Name
    # We set a minimum fallback width of 10 so the header "Class Name" always fits
    max_class_len = max(len(str(row.get("className", ""))) for row in resultsData)
    class_col_width = max(max_class_len, 10) 
    
    # 2. Define fixed widths for other standard columns
    id_w, sem_w, score_w = 4, 8, 6
    
    # 3. Calculate total width of the table contents to scale the borders perfectly
    # (Sum of padding spaces + column widths + vertical dividers)
    total_ui_width = 2 + id_w + 3 + class_col_width + 3 + sem_w + 3 + score_w + 2

    # Header UI
    print("\n" + "═" * total_ui_width)
    print(f"║ {'STUDENT ACADEMIC PERFORMANCE DASHBOARD'.center(total_ui_width - 4)} ║")
    print("═" * total_ui_width)
    
    # Table Column Headers
    print(f" │ {'ID':<{id_w}} │ {'Class Name':<{class_col_width}} │ {'Semester':<{sem_w}} │ {'Score':<{score_w}} │")
    print(f" ├{'─'* (id_w + 2)}┼{'─'* (class_col_width + 2)}┼{'─'* (sem_w + 2)}┼{'─'* (score_w + 2)}┤")

    total_score = 0
    
    # Loop through and print rows dynamically aligned
    for row in resultsData:
        r_id = row.get("resultId", "-")
        c_name = row.get("className", "Unknown")
        sem = f"Sem {row.get('semester', '-')}"
        score = row.get("score", 0)
        
        total_score += score
            
        print(f" │ {r_id:<{id_w}} │ {c_name:<{class_col_width}} │ {sem:<{sem_w}} │ {score:<{score_w}} │")

    # Footer UI & Summary Stats
    print(f" └{'─'* (id_w + 2)}┴{'─'* (class_col_width + 2)}┴{'─'* (sem_w + 2)}┴{'─'* (score_w + 2)}┘")
    
    # Calculate Average
    avg_score = total_score / len(resultsData)
    
    print("─" * total_ui_width)
    print(f"  Total Classes: {len(resultsData):<10} Average Score: {avg_score:.2f}%")
    print("═" * total_ui_width + "\n")