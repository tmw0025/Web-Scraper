import sys
from printers import MenuPrint

# Function to obtain semester choice
# Includes error handling on user input
def getSemester():

    validChoiceChosen = False
    while not validChoiceChosen:
        MenuPrint()
        userAns = input(">>> ") # Get user input

        if userAns.lower() == 'q': # If user wants to quit
            print("Goodbye!") # exit
            sys.exit()
        try:
            userAns = int(userAns) # try to convert user answer to integer
        except ValueError: # if it's all text
            print("Not a Number, please enter a valid integer.") # Try again
            continue
        validChoice = [1,2,3] # we could do range(1,4) actually.
        if userAns in validChoice: # if user input is valid
            validChoiceChosen = True # We get out.
            break
        if userAns not in validChoice:
            print("Invalid Number, please enter a valid integer.")
            continue
    return userAns