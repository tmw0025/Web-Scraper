from Course import Course

# This function will take the class list from the department and semester
# and then gives a class representation of the information. See class for it.
# TODO: Flesh this out so that it returns a Course object of each course listing.

def parseInformation(courseLine):
    course = Course()
    try:
        index = 0 # Skip some spaces
        course.sectionType = courseLine[:5]
        
        index += 5 # Skip some spaces
        course.CRN = int(courseLine[index:index + 5])
        
        index += 7 # Skip some spaces
        course.courseNumber = courseLine[index: index + 4]

        index += 4 # Skip some spaces
        course.courseId = int(courseLine[index: index + 3])

        index += 7 # Skip some spaces
        course.title = courseLine[index: index + 34]

        index += 34 # Skip some spaces
        course.creditHours = float(courseLine[index: index+3])
        
        index += 5 # Skip some spaces
        course.maxEnrolled = int(courseLine[index:index+3])
        
        index += 5 # Skip some spaces
        course.currEnrolled = int(courseLine[index:index+3])
        
        index += 14 # Skip some spaces
        course.waitlist = int(courseLine[index:index+3])
        
        index += 4 # Skip some spaces
        course.days = courseLine[index: index+5]
        
        index += 8 # Skip some spaces
        course.start = courseLine[index: index+7]
        
        index += 8 # Skip some spaces
        course.end = courseLine[index: index+7]
        
        index += 8 # Skip some spaces
        course.building = courseLine[index: index+4]
        
        index += 6 # Skip some spaces
        course.room = courseLine[index: index+6]
        
        index += 11 # Skip some spaces
        course.instructor = courseLine[index:]
        
    except ValueError:
        print("Error parsing course line!")
        return course
    return course