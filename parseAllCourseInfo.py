from parseInformation import parseInformation

# This function takes all of the course listings and
# parses each one and puts it into a list of Course objects
def parseAllCourseInfo(courseList):
    out = []
    for line in courseList:
        out.append(parseInformation(line))
    return out
