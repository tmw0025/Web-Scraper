from bs4 import BeautifulSoup
from urllib.request import urlopen


# Grabs all the information from the link
# Specifically all the classes and their information
def infoGrabber( linkList ):

    validCollegeLength = False

    #Check to make sure college entered is either 2 or 3 letters. 
    while validCollegeLength == False:
        college = str(input("Enter 2-3 letter college code for class(i.e. MA - Math, CPE - Computer Eng):"))
        if len(college) == 2 or len(college) == 3:
            validCollegeLength = True
        else:
            print("Not a college name, try again.")

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
