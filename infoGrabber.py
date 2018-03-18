from bs4 import BeautifulSoup
from urllib.request import urlopen
from parseInformation import parseInformation

# Grabs all the information from the link
# Specifically all the classes and their information
def infoGrabber( linkList ):

    validCollegeLength = False

    #Check to make sure college entered is either 2 or 3 letters. 
    while validCollegeLength == False:
        college = str(input("Enter 2-3 letter college code for class(i.e. MA - Math, CPE - Computer Eng):")).upper()
        if len(college) == 2 or len(college) == 3:
            validCollegeLength = True
        else:
            print("Not a college name, try again.")
    courseList = []
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
            for info in soup.find_all('pre'): # Find all pre tags and iterate through them
                for text in info.contents: # Check the contents of each pre tag
                    if text.find('Type') != -1 and text.find('<a') == -1 and text.find('<hr') == -1 and text is not None: # If the content of the iterated pre tag is a course list
                        for line in info.text.split('\n'): # Process the course list by line
                            if line.find(".0") != -1: # Find lines with course information
                                courseList.append(parseInformation(line)) # Parse information into classes and store them in a list
                                textList.append(line) # add line to textList to be printed
#    for course in courseList:
#        course.printInfo()       #  This is for testing purposes.
    return textList
