from bs4 import BeautifulSoup
from urllib.request import urlopen
from parseInformation import parseInformation

# Grabs all the information from the link
# Specifically all the classes and their information
def infoGrabber( link , semester):

    courseList = []
    # Go through each possible department in classes for the semester.
    if link.count('=') == 2:
        linkedCollege = link.split('=')
        major = linkedCollege[2]
        page = urlopen(link)
        # open the link and run it through BeautifulSoup
        soup = BeautifulSoup(page, 'html.parser')
        # For all links on page
        for info in soup.find_all('pre'): # Find all pre tags and iterate through them
            for text in info.contents: # Check the contents of each pre tag
                if text.find('Type') != -1 and text.find('<a') == -1 and text.find('<hr') == -1 and text is not None: # If the content of the iterated pre tag is a course list
                    for line in info.text.split('\n'): # Process the course list by line
                        if line.find(".0") != -1: # Find lines with course information
                            courseList.append(parseInformation(line, semester, major)) # Parse information into classes and store them in a list
    return courseList
