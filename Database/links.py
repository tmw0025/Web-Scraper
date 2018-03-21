from urllib.request import urlopen
from bs4 import BeautifulSoup
from getAllCourses import  getAllCourses

# Function that grabs links from specified url and puts them into a list
def linkGrabber( pageUrl , linkList ):
    page = urlopen(pageUrl)
    # TODO: Is there a way that we can have a single BeautifulSoup object?
    soup = BeautifulSoup(page, 'html.parser')

    # For every link in the page
    for links in soup.find_all('a'):
        if links.get('href') is not None:
            linkList.append(links.get('href'))
    linkList = getAllCourses(linkList)
    return

# Formats links so that they go to cgi-bin with the correct URL
def linkFormatter( linkList ):
    for i,links in enumerate(linkList):
        url = "http://www.uah.edu" + links
        linkList[i] = url

    return

