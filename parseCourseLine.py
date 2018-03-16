# This parses an individual course line and returns the line if it is a course
# otherwise it prints an empty line
def parseCourseLine(line):

    lenOfActualLine = 161 # TODO: Don't let this be hardcoded.
    crnText = line[5:10] # The CRN should be within this position
    try:
        crn = int(crnText)  # Try to convert the text to a number, which would happen
                            # if the line contained an actual course
        return line # If it did, return the line
    except ValueError: # If the line doesn't have a CRN
        return "" # return basically nothing
