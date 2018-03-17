from parseInformation import parseInformation

def parseAllCourseInfo(courseList):
    out = []
    for line in courseList:
        out.append(parseInformation(line))
    return out
