import sqlite3
from sqlite3 import Error
from links import linkFormatter, linkGrabber
from infoGrabber import infoGrabber
from Course import Course

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

        return None


def create_tables(conn):
    try:
        c = conn.cursor()
        college_table = ''' CREATE TABLE IF NOT EXISTS colleges(
                                major text,
                                link text,
                                semester text 
                            );'''
        c.execute(college_table)
        course_table = ''' CREATE TABLE IF NOT EXISTS courses(
                                major_id text,
                                semester_id text,
                                sectiontype text,
                                crn integer,
                                coursenum text,
                                courseid integer,
                                title text,
                                credithrs integer,
                                maxenrolled integer,
                                currentenrolled integer,
                                days text,
                                waitlist integer,
                                starttime text,
                                endtime text,
                                building text,
                                room integer,
                                instructor text
                            );'''
        c.execute(course_table)
    except Error as e:
        print(e)
    return


def create_courses(conn, courseList):
    for course in courseList:
        create_course(conn, course)
    return


def create_course(conn, course):
    sql = ''' INSERT INTO courses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''
    cur = conn.cursor()
    info = course.getTuple()
    print(info)
    cur.execute(sql, info)
    return cur.lastrowid


def main():
    pageQuote = "https://www.uah.edu/cgi-bin/schedule.pl?"
    mainLinks = []  # Links on the main page.
    springLinks = []  # Links on the spring semester page
    summerLinks = []  # Links on the summer semester page
    fallLinks = []  # Links on the fall semester page
    database = "Course_Catalogue.db"
    conn = create_connection(database)

    with conn:
        create_tables(conn)
        # Grab the links on the main page
        linkGrabber(pageQuote, mainLinks)

        # Go through each possible link and try to find each semester within each.
        for links in mainLinks:

            if links.find('sprg') != -1:  # we could do >= 0
                linkGrabber(links, springLinks)
                linkFormatter(springLinks)


            if links.find("sum") != -1:
                linkGrabber(links, summerLinks)
                linkFormatter(summerLinks)

            if links.find("fall") != -1:
                linkGrabber(links, fallLinks)
                linkFormatter(fallLinks)

        for links in springLinks:
            create_courses(conn, infoGrabber(links, "Spring"))
        for links in summerLinks:
            create_courses(conn, infoGrabber(links, "Summer"))
        for links in fallLinks:
            create_courses(conn, infoGrabber(links, "Fall"))
if __name__ == '__main__':
    main()
