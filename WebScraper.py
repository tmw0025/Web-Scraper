
# WebScraper by the UAH CS Club


####################
#     Imports      #
####################
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys #for exiting
import os

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
    soup = BeautifulSoup(page, 'html.parser')

    for links in soup.find_all('a'):
        if links.get('href') is not None:
            linkList.append(links.get('href'))
    return;

def linkFormatter( linkList ):
    for i,links in enumerate(linkList):
        url = "http://www.uah.edu" + links
        linkList[i] = url
    
    return;

# Grabs all the information from the link
# Specifically all the classes and their information
def infoGrabber( linkList ):
    college = str(input("Enter 2-3 letter college code for class(i.e. MA - Math, CPE - Computer Eng):"))

    for links in linkList:
        if links.find(college) != -1:
            print(links)
            page = urlopen(links)
            soup = BeautifulSoup(page, 'html.parser')
            for info in soup.find_all('a'):
                if info is None or info.pre is None:
                    print("ERROR: Can't grab information.")
                    # TODO: Fill this out.
                elif info.pre.text is not None:
                    print(info.pre.text)


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

    pageQuote = "https://www.uah.edu/cgi-bin/schedule.pl?"

    mainLinks = []
    springLinks = []
    summerLinks = []
    fallLinks = []

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

    #Cleaner way of infoGrabber
    semesterLinkLists = [springLinks, summerLinks, fallLinks]
    infoGrabber(semesterLinkLists[userAns - 1])

####################
#       Main       #
####################

if __name__=="__main__":
    main()
