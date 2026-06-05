from src.Auth import login
from src.CSVFunctions import openCSV

# Loopable auth
# User login
# Loopable options until logout OR close app

# Case A: Logout 
# Loop auth

# Case B: Close App
# Exit completely

def main():
    # Variables
    notLoggedIn = False

    # Start up of the program
    while not notLoggedIn:
        txt = "Welcome to Student Marks Management System"
        border = "*" * (len(txt) + 4)
        programName = f"{border}\n* {txt} *\n{border}"

        # Show program MOTD
        print(programName)
        
        # Calls login function from src/Auth.py
        sessionData = login()["data"]

        # Check if sessionData dict is empty
        if not sessionData: 
            continue

        # Show program MOTD 2
       
        
        # Loops options infinitely until user logs out OR shutdown app
        while True: 
            print(programName)
            print(f"""
                1. Feature #1
                2. Feature #2
                3. Feature #3
                999. Log out as {sessionData['username']}
                1000. Close Appliction
            """)
            
            selectedOption = input("Select an option: ")
            match selectedOption:
                case "1":
                    print("Feature #1")
                case "2":
                    print("Feature #2")
                case "3":
                    print("Feature #3")                
                case "999":
                    break
                case "1000": # Exits whole program
                    exit()

main()