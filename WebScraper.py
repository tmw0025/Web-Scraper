from urllib.request import urlopen
from bs4 import BeautifulSoup

def linkGrabber( pageUrl , linkList ): #Function that grabs links from specified url and puts them into a list
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

def infoGrabber( linkList ):
    college = str(input("Enter 2-3 letter college code for class(i.e. MA for math):"))
    for links in linkList:
        if links.find(college) != -1:
            print(links)
            page = urlopen(links)
            soup = BeautifulSoup(page, 'html.parser')
            for info in soup.find_all('a'):
                if info.pre is not None:
                    for text in info.pre.contents:
                        if text.find('Sec') != -1:
                            print(text)
                
        
    return;

pageQuote = "https://www.uah.edu/cgi-bin/schedule.pl?"

mainLinks = []
springLinks = []
summerLinks = []
fallLinks = []

linkGrabber( pageQuote , mainLinks)

for links in mainLinks:
    
    if links.find('sprg') != -1:
        linkGrabber(links, springLinks)
        
    if links.find("sum") != -1:
        linkGrabber(links, summerLinks)

    if links.find("fall") != -1:
        linkGrabber(links, fallLinks)

linkFormatter(springLinks)
linkFormatter(summerLinks)
linkFormatter(fallLinks)

userAns = int(input("What semester would you like to view classes for?\n1.Spring\n2.Summer\n3.Fall\n\nEnter an interger(1-3):"))


if userAns == 1:
    infoGrabber(springLinks)
elif userAns == 2:
    infoGrabber(summerLinks)
elif userAns == 3:
    infoGrabber(fallLinks)
else:
    print("Invalid input. Ending program.\n")
    



