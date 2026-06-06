from time import sleep

from libs.libs import clearTerminal
from libs.types import TRole, TSessionData
from src.Auth import login, register

# Loopable auth
# User login
# Loopable options until logout OR close app

# Case A: Logout 
# Loop auth

# Case B: Close App
# Exit completely


# Variables
role: TRole = None

# Functions
def getMOTD():   
    txt = "Welcome to Student Marks Management System"
    borderLength = len(txt) + 4
    topBorder = "*" * borderLength
 
    # Dynamically read the current state of 'role'
    sessionTxt = f" SESSION: {role.upper() if role else None} "
    bottom_border = sessionTxt.center(borderLength, "*")
    programName = f"{topBorder}\n* {txt} *\n{bottom_border if role else topBorder}"
    return programName, topBorder

def main():
    # Start up of the program
    startUpWindow()

def startUpWindow():
    global role
    while True:
  
        # Show program MOTD & login/register options
        programName, topBorder = getMOTD()
        motdMsg = f"""{programName}
                1. Register
                2. Login
                1000. Close Application
                {topBorder}\n"""
        print("\n".join(line.lstrip() for line in motdMsg.splitlines()))

        selectedOption = input("\nSelect an option: ")
        
        match selectedOption.lower():
            case "1" | "register": # Register
                while True:
                    response = register()

                    # If successful registration, go back to startUpWindow for users to login
                    if response["success"]:
                        break
                    elif not response["success"]:
                        print(response["message"])


            case "2" | "login" : # Login 
                 while True:
                    print(programName)
                    # Calls login function from src/Auth.py
                    response = login()
                    
                    # Check if sessionData dict is empty
                    if not response["success"]:
                        # "Clears" terminal before printing MOTD & options
                        clearTerminal()
                        # print("[!] Username/password you have entered is incorrect!")
                        print(response["message"])
                        sleep(1.5)
                        clearTerminal()
                        continue
                    
                    if response["success"]:
                        clearTerminal()
                        print(response["message"])
                        sleep(1.5)
                        clearTerminal()
                        role = response["data"]["role"]

                    # If loggedInWindow function returns False, breaks the loop (Goes back to very first loop of startUpWindow)
                    if not loggedInWindow(response["data"]): 
                        role = None
                        break
            case "1000" | "exit" | "close" | "off": # Exits whole program
                exit()
    

def loggedInWindow(sessionData: TSessionData | dict):
    match sessionData["role"]:
        case "Admin":
            adminPage(sessionData)
        case "Student":
            studentPage(sessionData)
        case "Lecturer":
            adminPage(sessionData)

def studentPage(sessionData: TSessionData | dict):
    # Loops options infinitely until user logs out OR shutdown app
    while True: 
    # Show program MOTD & options
        programName, topBorder = getMOTD()
        motdMsg = f"""{programName}
            1. View results
            2. Export Results
            3. Feature #3
            999. Log out as {sessionData['username']} {f"({sessionData["name"]})"}
            1000. Close Application
            {topBorder}\n"""
        print("\n".join(line.lstrip() for line in motdMsg.splitlines()))
                
        selectedOption = input("\nSelect an option: ")

        match selectedOption:
            case "1":
                print("Feature #1")
            case "2":
                print("Feature #2")
            case "3":
                print("Feature #3")                
            case "999":
                return False
                break
            case "1000" | "exit" | "close" | "off": # Exits whole program
                exit()

def lecturerPage(sessionData: TSessionData | dict):
    # Loops options infinitely until user logs out OR shutdown app
    while True: 
    # Show program MOTD & options
        programName, topBorder = getMOTD()
        motdMsg = f"""{programName}
            1. Feature #1
            2. Feature #2
            3. Feature #3
            999. Log out as {sessionData['username']} {f"({sessionData["name"]})"}
            1000. Close Application
            {topBorder}\n"""
        print("\n".join(line.lstrip() for line in motdMsg.splitlines()))
                
        selectedOption = input("\nSelect an option: ")

        match selectedOption:
            case "1":
                print("Feature #1")
            case "2":
                print("Feature #2")
            case "3":
                print("Feature #3")                
            case "999":
                return False
                break
            case "1000" | "exit" | "close" | "off": # Exits whole program
                exit()

def adminPage(sessionData: TSessionData | dict):
    # Loops options infinitely until user logs out OR shutdown app
    while True: 
    # Show program MOTD & options
        programName, topBorder = getMOTD()
        motdMsg = f"""{programName}
            1. Feature #1
            2. Feature #2
            3. Feature #3
            999. Log out as {sessionData['username']} {f"({sessionData["name"]})"}
            1000. Close Application
            {topBorder}\n"""
        print("\n".join(line.lstrip() for line in motdMsg.splitlines()))
                
        selectedOption = input("\nSelect an option: ")

        match selectedOption:
            case "1":
                print("Feature #1")
            case "2":
                print("Feature #2")
            case "3":
                print("Feature #3")                
            case "999":
                return False
                break
            case "1000" | "exit" | "close" | "off": # Exits whole program
                exit()

# The function to start the whole program
main()