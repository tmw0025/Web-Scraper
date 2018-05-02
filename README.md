# Web-Scraper(Moved to CS branch)

This project is to get information from the UAH cgi-bin that lists all of the classes for each semester that will be offered at UAH. We will setup the main web-scraper, then put that information into a database using a flavor of SQL, then create an API that will allow future projects to use this application.

To-do List:
* Fix indexing in parseInformation
* Improve database functionality
* Provide access to database through an API - written in Python

Done List:
* Parse information from requests and store it into Course class
* Save Course Class into a database entry
