import sqlite3
from sqlite3 import Error

from infoGrabber import infoGrabber
from links import linkGrabber, linkFormatter


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

        c.execute( ''' CREATE TABLE IF NOT EXISTS springcolleges(
                                id INTEGER PRIMARY KEY,
                                major text,
                                link text
                            );''')
        c.execute( ''' CREATE TABLE IF NOT EXISTS summercolleges(
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
                                        collegeid integer,
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
                                        FOREIGN KEY (collegeid) REFERENCES summercolleges(id)
                                    );''')
        c.execute(''' CREATE TABLE IF NOT EXISTS fallcourses(
                                        collegeid integer,
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
                                        FOREIGN KEY (collegeid) REFERENCES fallcolleges(id)
                                    );''')
    except Error as e:
        print(e)
    return


def create_courses(conn, courseList, s, i):
    for course in courseList:
        create_course(conn, course, s, i)

    return


def create_course(conn, course, s, id):
    if s == "Spring":
        sql = ''' INSERT INTO springcourses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''
        cur = conn.cursor()
        info = course.getTuple()+(id,)
        print(info)
        cur.execute(sql, info)
        return cur.lastrowid
    elif s == "Summer":
        sql = ''' INSERT INTO summercourses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''
        cur = conn.cursor()
        info = course.getTuple()
        print(info)
        cur.execute(sql, info)
        return cur.lastrowid
    elif s == "Fall":
        sql = ''' INSERT INTO fallcourses VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''
        cur = conn.cursor()
        info = course.getTuple()
        print(info)
        cur.execute(sql, info)
        return cur.lastrowid

def main():
    i = 0
    pageQuote = "https://www.uah.edu/cgi-bin/schedule.pl?"
    mainLinks = []  # Links on the main page.
    springLinks = []  # Links on the spring semester page
    summerLinks = []  # Links on the summer semester page
    fallLinks = []  # Links on the fall semester page
    database = "Course_Catalogue.db"
    conn = create_connection(database)

    with conn:
        conn.execute("PRAGMA FOREIGN_KEYS = 1")
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
            if links.count('=') == 2:
                i += 1
                create_courses(conn, infoGrabber(links), "Spring", i)
        i = 0
        for links in summerLinks:
            if links.count('=') == 2:
                i += 1
                create_courses(conn, infoGrabber(links), "Summer", i)
        i = 0
        for links in fallLinks:
            if links.count('=') == 2:
                i += 1
                create_courses(conn, infoGrabber(links), "Fall", i)


if __name__ == '__main__':
    main()
