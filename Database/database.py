import sqlite3
from sqlite3 import Error

from infoGrabber import infoGrabber
from links import linkGrabber, linkFormatter


def create_connection(db_file):
    # Connects a database file. If one isn't found, it will create one.
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:  # Error if something goes horribly wrong.
        print(e)

        return None


def create_tables(conn):
    # Create tables for colleges and courses for each semester.
    try:
        c = conn.cursor()  # Set c as SQLite cursor. The cursor is used to execute SQLite commands and allows the
        # ability to receive results from the database.
        c.execute(''' CREATE TABLE IF NOT EXISTS springcolleges(
                                id INTEGER PRIMARY KEY,
                                major text,
                                link text
                            );''')
        c.execute(''' CREATE TABLE IF NOT EXISTS summercolleges(
                                id integer primary key,
                                major text,
                                link text
                            );''')
        c.execute(''' CREATE TABLE IF NOT EXISTS fallcolleges(
                                id integer primary key,
                                major text,
                                link text
                            );''')

        c.execute(''' CREATE TABLE IF NOT EXISTS springcourses(
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
                                instructor text,
                                collegeid integer,
                                FOREIGN KEY (collegeid) REFERENCES springcolleges(id)
                            );''')
        c.execute(''' CREATE TABLE IF NOT EXISTS summercourses(
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
                                        instructor text,
                                        collegeid integer,
                                        FOREIGN KEY (collegeid) REFERENCES summercolleges(id)
                                    );''')
        c.execute(''' CREATE TABLE IF NOT EXISTS fallcourses(
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
                                        instructor text,
                                        collegeid integer,
                                        FOREIGN KEY (collegeid) REFERENCES fallcolleges(id)
                                    );''')
    except Error as e:
        print(e)
    return


def create_colleges(conn, link, sem, collegeid):
    # Function that takes a college course link with a connection, a semester, and a college id and inserts the id,
    # college offering the courses, and the link to the page into a row in the semester specified colleges table
    if sem == "Spring":
        linkedCollege = link.split(
            '=')  # Splits link by = character into a list. The current links all end with their linked major which comes directly after the second equals
        major = linkedCollege[2]  # Select the college code. This is inserted as college name in springcolleges table
        sql = ''' INSERT INTO springcolleges VALUES(?,?,?); '''  # SQLite command for inserting into springcolleges table.
        cur = conn.cursor()  # Set cur as SQLite cursor.
        info = (collegeid, major, link)  # Make a tuple for inserting values into sql string.
        cur.execute(sql, info)  # Execute command
    if sem == "Summer":  # Rinse and repeat for summercolleges table and springcolleges table
        linkedCollege = link.split('=')
        major = linkedCollege[2]
        sql = ''' INSERT INTO summercolleges VALUES(?,?,?); '''
        cur = conn.cursor()
        info = (collegeid, major, link)
        cur.execute(sql, info)
    if sem == "Fall":
        linkedCollege = link.split('=')
        major = linkedCollege[2]
        sql = ''' INSERT INTO fallcolleges VALUES(?,?,?); '''
        cur = conn.cursor()
        info = (collegeid, major, link)
        cur.execute(sql, info)
    # print(info)  # Uncomment this for terminal viewing of progress. Might affect performance.
    return


def create_courses(conn, courselist, s, id):
    # Function that takes a lists of courses with a connection, a semester,
    # and a college id and inserts the course information to a row in semester specified
    for course in courselist:
        if s == "Spring":
            sql = ''' INSERT INTO springcourses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''  # SQLite command for inserting into spring courses table.
            cur = conn.cursor()  # Set cur as SQLite cursor.
            info = course.getTuple() + (
            id,)  # Use course object function to get info in tuple form while concatenating the college id onto it.
            cur.execute(sql, info)  # Execute command
        elif s == "Summer":  # Rinse and repeat for summercourses and fallcourses
            sql = ''' INSERT INTO summercourses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''
            cur = conn.cursor()
            info = course.getTuple() + (id,)
            cur.execute(sql, info)
        elif s == "Fall":
            sql = ''' INSERT INTO fallcourses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''
            cur = conn.cursor()
            info = course.getTuple() + (id,)
            cur.execute(sql, info)
        # print(info)  # Uncomment this for terminal viewing of progress. Might affect performance.

    return cur.lastrowid


def main():
    # TODO General reformatting and cleaning
    # TODO Functions for selecting based off criteria such as college, semester, ect.
    # TODO Ability to update if existing database is detected and is out of date

    i = 0  # This is for the college id, which is used to link courses to the college offering them
    pageQuote = "https://www.uah.edu/cgi-bin/schedule.pl?"  # Scraping link
    mainLinks = []  # Links on the main page.
    springLinks = []  # Links on the spring semester page
    summerLinks = []  # Links on the summer semester page
    fallLinks = []  # Links on the fall semester page
    database = "Course_Catalogue.db"  # Name of database
    conn = create_connection(database)

    with conn:
        conn.execute(
            "PRAGMA FOREIGN_KEYS = 1")  # SQLite command for enabling foreign keys, which are used to link tables.
        create_tables(conn)  # Create all required tables
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
            if links.count('=') == 2:  # Ensure that the link is a college courses page.
                i += 1  # Increment college id
                create_colleges(conn, links, "Spring", i)  # Fill out springcolleges table
                create_courses(conn, infoGrabber(links), "Spring", i)  # Fill out spring courses table
        i = 0  # Reset id counter for reuse in summerLinks and fallLinks loops.
        for links in summerLinks:
            if links.count('=') == 2:
                i += 1
                create_colleges(conn, links, "Summer", i)
                create_courses(conn, infoGrabber(links), "Summer", i)
        i = 0
        for links in fallLinks:
            if links.count('=') == 2:
                i += 1
                create_colleges(conn, links, "Fall", i)
                create_courses(conn, infoGrabber(links), "Fall", i)


if __name__ == '__main__':
    main()
