from time import sleep

from libs.libs import clearTerminal
from libs.types import TSessionData
from src.Auth import login, register

# Loopable auth
# User login
# Loopable options until logout OR close app

# Case A: Logout 
# Loop auth

# Case B: Close App
# Exit completely


# Variables
txt = "Welcome to Student Marks Management System"
border = "*" * (len(txt) + 4)
programName = f"{border}\n* {txt} *\n{border}"

# Functions
def main():
    # Start up of the program
    startUpWindow()

def startUpWindow():
    while True:
        # Show program MOTD & login/register options
        motdMsg = f"""{programName}
                1. Register
                2. Login
                1000. Close Application
                {border}\n"""
        print("\n".join(line.lstrip() for line in motdMsg.splitlines()))

        selectedOption = input("\nSelect an option: ")
        
        match selectedOption:
            case "1": # Register
                while True:
                    response = register()
            case "2": # Login 
                 while True:
                    print(programName)
                    # Calls login function from src/Auth.py
                    response = login()
                    
                    # Check if sessionData dict is empty
                    if not response["data"]:
                        # "Clears" terminal before printing MOTD & options
                        clearTerminal()
                        # print("[!] Username/password you have entered is incorrect!")
                        print(response["message"])
                        sleep(1.5)
                        clearTerminal()
                        continue

                    # If loggedInWindow function returns False, breaks the loop (Goes back to very first loop of startUpWindow)
                    if not loggedInWindow(response["data"]):
                        break
            case "1000": 
                exit()
    

def loggedInWindow(sessionData: TSessionData | dict):
    # Loops options infinitely until user logs out OR shutdown app
    while True: 
    # Show program MOTD & options
        motdMsg = f"""{programName}
            1. Feature #1
            2. Feature #2
            3. Feature #3
            999. Log out as {sessionData['username']}
            1000. Close Application
            {border}\n"""
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
            case "1000": # Exits whole program
                exit()


# The function to start the whole program
main()