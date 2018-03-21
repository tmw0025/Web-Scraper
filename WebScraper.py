
# WebScraper by the UAH CS Club


####################
#     Imports      #
####################
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys #for exiting



#Imports from other files
from Course import Course
from parseInformation import parseInformation
from parseCourseLine import parseCourseLine
from printers import PrintHeader, MenuPrint
from links import linkGrabber, linkFormatter
from getSemester import getSemester
from infoGrabber import infoGrabber
from getAllCourses import getAllCourses
from parseAllCourseInfo import parseAllCourseInfo


# BeautifulSoup Tutorial
# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe



########################
# Function Definitions #
########################

# Main function.
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
        coursesClassList = parseAllCourseInfo(courses)
        print("\n{} results found!\n".format(len(coursesClassList)))
        for course in coursesClassList:
            course.printInfo()

        #Ask user if they want to try again
        if input("Press q to exit, press any other key to search again.").lower() == "q":
            exitFlag = True

####################
#       Main       #
####################

if __name__=="__main__":
    main()
