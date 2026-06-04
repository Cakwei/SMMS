from CSVFunctions import openCSV

def main():
    # Start up of the program
    txt = "Welcome to Student Marks Management System"
    border = "*" * (len(txt) + 4)
    programName = f"{border}\n* {txt} *\n{border}"

    print(programName)

main()