
# WebScraper by the UAH CS Club


####################
#     Imports      #
####################
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys #for exiting
import os
from Course import Course

# BeautifulSoup Tutorial
# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe



########################
# Function Definitions #
########################

# This function will take the class list from the department and semester
# and then gives a class representation of the information. See class for it.
# TODO: Flesh this out as well.
def parseInformation():
    return

def linkGrabber( pageUrl , linkList ): # Function that grabs links from specified url and puts them into a list
    page = urlopen(pageUrl)
    # TODO: Is there a way that we can have a single BeautifulSoup object?
    soup = BeautifulSoup(page, 'html.parser')

    for links in soup.find_all('a'):
        if links.get('href') is not None:
            linkList.append(links.get('href'))
    return;

# Formats links so that they go to cgi-bin with the correct URL
def linkFormatter( linkList ):
    for i,links in enumerate(linkList):
        url = "http://www.uah.edu" + links
        linkList[i] = url

    return;

# Grabs all the information from the link
# Specifically all the classes and their information
def infoGrabber( linkList ):
    college = str(input("Enter 2-3 letter college code for class(i.e. MA - Math, CPE - Computer Eng):"))

    # Go through each possible department in classes for the semester.
    for links in linkList:
        # If we found the college the user wants
        if links.find(college) != -1:
            print(links)
            page = urlopen(links)
            # open the link and run it through BeautifulSoup
            soup = BeautifulSoup(page, 'html.parser')
            # For all links on page
            for info in soup.find_all('a'):
                # If the link doesn't have a pre tag (meaning it doesn't have the classes)
                if info is None or info.pre is None:
                    # Ignore it and move on.
                    continue
                elif info.pre.text is not None: # If the link does have the classes
                    print(info.pre.text) # Print all the info


# Prints the possible semesters that the college offers
# TODO: Maybe make it so that if there is only one semester available for viewing, it prints that one.
def MenuPrint():
    print("What semester would you like to view classes for? Hit q to exit")
    semesterList = ["Spring", "Summer", "Fall"]

    idx = 1
    for semester in semesterList:
        print ('{}. {}'.format(idx,semester))
        idx += 1

# Function to obtain semester choice
# Includes error handling on user input
def getSemester():

    validChoiceChosen = False
    while not validChoiceChosen:
        MenuPrint()
        userAns = input(">>> ")

        if userAns == 'q':
            print("Goodbye!")
            sys.exit()
        try:
            userAns = int(userAns)
        except ValueError:
            print("Not a Number, please enter a valid integer.")
            continue
        validChoice = [1,2,3] # we could do range(1,4) actually.
        if userAns in validChoice:
            validChoiceChosen = True
            break
        if userAns not in validChoice:
            print("Invalid Number, please enter a valid integer.")
            continue
    return userAns

def PrintHeader():

    # Clear terminal and print header
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the cgi-bin scraper. \n\n\n")


def main():

    PrintHeader()

    exitFlag = False
    while exitFlag == False:
        pageQuote = "https://www.uah.edu/cgi-bin/schedule.pl?"

        mainLinks   = []    # Links on the main page.
        springLinks = []    # Links on the spring semester page
        summerLinks = []    # Links on the summer semester page
        fallLinks   = []    # Links on the fall semester page

        # Grab the links on the main page
        linkGrabber( pageQuote , mainLinks)

        # Go through each possible link and try to find each semester within each.
        for links in mainLinks:

            if links.find('sprg') != -1: # we could do >= 0
                linkGrabber(links, springLinks)

            if links.find("sum") != -1:
                linkGrabber(links, summerLinks)

            if links.find("fall") != -1:
                linkGrabber(links, fallLinks)

        linkFormatter(springLinks)
        linkFormatter(summerLinks)
        linkFormatter(fallLinks)

        # Cue for input from user
        userAns = getSemester()

        # Cleaner way of infoGrabber
        semesterLinkLists = [springLinks, summerLinks, fallLinks]
        infoGrabber(semesterLinkLists[userAns - 1])





        #Ask user if they want to try again
        if input("Press q to exit, press any other key to search again.").lower() == "q":
            exitFlag = True

####################
#       Main       #
####################

if __name__=="__main__":
    main()
