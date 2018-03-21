# This class contains the information for the class
# Such as: CRN, Course Num:Id, Title, Credit, Max Enrollment,
# Enrolled, Available, Waitlist Count, Days, Start, End, Building
# Room number, Instructor, Section Type

class Course:

    def __init__(self):
        self.semester = ""
        self.major = ""
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
        self.room = 0
        self.instructor = ""

    def getAvailable(self):
        out = self.maxEnrolled - self.currEnrolled
        if out < 0:
            out = 0
        return out

    # This Function is used in infoGrabber for testing
    def printInfo(self):
        print("Section: ", self.sectionType, " CRN: ", self.CRN,
              " Course Number: ", self.courseNumber, " Course ID: ",
              self.courseId, " Title: ", self.title, " Credit Hours: ",
              self.creditHours, " Max Enrolled: ", self.maxEnrolled,
              " Current Enolled: ", self.currEnrolled, " Waitlist: ",
              self.waitlist, " Days: ", self.days, " Start: ", self.start,
              " End: ", self.end, " Building: ", self.building, " Room: ",
              self.room, " Instructor: ", self.instructor)
      
        return

    def getTuple(self):
        tup = (self.major, self.semester, self.sectionType, self.CRN,
               self.courseNumber, self.courseId, self.title, self.creditHours,
               self.maxEnrolled, self.currEnrolled, self.days, self.waitlist,
               self.start, self.end, self.building, self.room, self.instructor)
        return tup
