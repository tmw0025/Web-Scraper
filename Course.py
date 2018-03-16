# This class contains the information for the class
# Such as: CRN, Course Num:Id, Title, Credit, Max Enrollment,
# Enrolled, Available, Waitlist Count, Days, Start, End, Building
# Room number, Instructor, Section Type

class Course:

    def __init__(self):
        self.sectionType = ""
        self.CRN = 0
        self.courseNumber = "" 
        self.courseId = 0
        self.title = ""
        self.creditHours = 0
        self.maxEnrolled = 0
        self.currEnrolled = 0
        self.days = ""
        self.waitlist = 0
        self.start = ""
        self.end = ""
        self.building = ""
        self.room = ""
        self.instructor = ""

    def getAvailable(self):
        out = self.maxEnrolled - self.currEnrolled
        if out < 0:
            out = 0
        return out

##    def printInfo(self): This Function is used in infoGrabber for testing
##        print("Section:", self.sectionType, " CRN:", self.CRN, " Course Number:", self.courseNumber, " Course ID:", self.courseId, " Title:", self.title, " Credit Hours:", self.creditHours, " Max Enrolled:", self.maxEnrolled, " Current Enolled:", self.currEnrolled, " Waitlist:", self.waitlist, " Days:", self.days, " Start:", self.start, " End:", self.end, " Building:", self.building, " Room:", self.room, " Instructor:", self.instructor)
        
