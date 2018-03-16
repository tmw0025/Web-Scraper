# This function will take the class list from the department and semester
# and then gives a class representation of the information. See class for it.
# TODO: Flesh this out so that it returns a Course object of each course listing.
def parseInformation(courseLine):
    course = Course()
    try:
        index = 0
        course.sectionType = courseLine[:5]
        index += 5
        course.CRN = int(courseLine[index:index + 5])
        index += 5
        # Skip some spaces
        course.courseNumber = int(courseLine[index: index + 3])
        index += 3

        # Skip some spaces
        index += 1
        course.courseId = int(courseLine[index: index + 2])

        # Skip some spaces
        index += 5
        course.title = courseLine[index: index + 34]

        index += 34


        course.courseNumber = int()
    except ValueError:
        print("Error parsing course line!")
        return course
    return course