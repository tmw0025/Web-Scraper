import os

def PrintHeader():
    # Clear terminal and print header
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the cgi-bin scraper. \n\n\n")


# Prints the possible semesters that the college offers
# TODO: Maybe make it so that if there is only one semester available for viewing, it prints that one.
def MenuPrint():
    print("What semester would you like to view classes for? Hit q to exit")
    semesterList = ["Spring", "Summer", "Fall"]

    idx = 1
    for semester in semesterList:
        print ('{}. {}'.format(idx,semester)) # Print all semesters.
        idx += 1