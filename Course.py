# This class contains the information for the class
# Such as: CRN, Course Num:Id, Title, Credit, Max Enrollment,
# Enrolled, Available, Waitlist Count, Days, Start, End, Building
# Room number, Instructor, Section Type

class Course:

    def __init__(self):
        self.sectionType = ""
        self.CRN = 0
        self.courseNumber = 0
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
