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
                if info.pre.text is not None:
                    print(info.pre.text)
                
        
    return;


def MenuPrint():
    print("What semester would you like to view classes for?")
    semesterList = ["Spring", "Summer", "Fall"]

    idx = 1
    for semester in semesterList:
        print ('{}.\t{}'.format(idx,semester))
        idx = idx + 1

def getSemester():
    userAns = input(">>> ")
    validChoiceChosen = 0
    while validChoiceChosen==0:
        try:
            userAns = int(userAns)
        except ValueError:
            print("Not a Number")
            MenuPrint()
            userAns = input(">>> ")
        validChoice = [1,2,3]
        if userAns in validChoice:
            validChoiceChosen = 1
            break
        else:
            print("Invalid Number.")
            MenuPrint()
            userAns = input(">>> ")
    return userAns

def main():
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



    #print out the menu
    MenuPrint()


    #Cue for input from user
    userAns = getSemester()


    #TODO error checking on input
    if userAns == 1:
        infoGrabber(springLinks)
    elif userAns == 2:
        infoGrabber(summerLinks)
    elif userAns == 3:
        infoGrabber(fallLinks)
    # else:
    #     print("Invalid input. Ending program.\n")
        


if __name__=="__main__":
    main()
