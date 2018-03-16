
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
# TODO: Flesh this out so that it returns a Course object of each course listing.
def parseInformation(courseLine):
    course = Course()
    try:
        index = 0
        course.sectionType = courseLine[:5]
        index += 5
        course.CRN = int(courseLine[index:index + 5])
        index += 5
        # Skip some spaces
        course.courseNumber = int(courseLine[index: index + 3])
        index += 3

        # Skip some spaces
        index += 1
        course.courseId = int(courseLine[index: index + 2])

        # Skip some spaces
        index += 5
        course.title = courseLine[index: index + 34]

        index += 34


        course.courseNumber = int()
    except ValueError:
        print("Error parsing course line!")
        return course
    return course


# This parses an individual course line and returns the line if it is a course
# otherwise it prints an empty line
def parseCourseLine(line):

    lenOfActualLine = 161 # TODO: Don't let this be hardcoded.
    crnText = line[5:10] # The CRN should be within this position
    try:
        crn = int(crnText)  # Try to convert the text to a number, which would happen
                            # if the line contained an actual course
        return line # If it did, return the line
    except ValueError: # If the line doesn't have a CRN
        return "" # return basically nothing


# Returns all courses from the course listing.
def getAllCourses(textList):
    out = []
    # For each line in the course listing table
    for line in textList:
        courseLine = parseCourseLine(line)
        if len(courseLine) > 0: # If the course actually has something
            out.append(courseLine) # Add the course to our output.
    return out


def linkGrabber( pageUrl , linkList ): # Function that grabs links from specified url and puts them into a list
    page = urlopen(pageUrl)
    # TODO: Is there a way that we can have a single BeautifulSoup object?
    soup = BeautifulSoup(page, 'html.parser')

    # For every link in the page
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

    textList = []
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
                    for line in info.pre.text.split('\n'):
                        textList.append(line)
    return textList

# Prints the possible semesters that the college offers
# TODO: Maybe make it so that if there is only one semester available for viewing, it prints that one.
def MenuPrint():
    print("What semester would you like to view classes for? Hit q to exit")
    semesterList = ["Spring", "Summer", "Fall"]

    idx = 1
    for semester in semesterList:
        print ('{}. {}'.format(idx,semester)) # Print all semesters.
        idx += 1

# Function to obtain semester choice
# Includes error handling on user input
def getSemester():

    validChoiceChosen = False
    while not validChoiceChosen:
        MenuPrint()
        userAns = input(">>> ") # Get user input

        if userAns == 'q': # If user wants to quit
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
        courseListings = infoGrabber(semesterLinkLists[userAns - 1])
        courses = getAllCourses(courseListings)
        for course in courses:
            print(course)




        #Ask user if they want to try again
        if input("Press q to exit, press any other key to search again.").lower() == "q":
            exitFlag = True

####################
#       Main       #
####################

if __name__=="__main__":
    main()
