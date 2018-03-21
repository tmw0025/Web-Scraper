from parseCourseLine import parseCourseLine


# Returns all courses from the course listing.
def getAllCourses(textList):
    out = []
    # For each line in the course listing table
    for line in textList:
        courseLine = parseCourseLine(line)
        if len(courseLine) > 0: # If the course actually has something
            out.append(courseLine) # Add the course to our output.
    return out
