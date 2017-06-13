#!/usr/bin/env python2.7

import psycopg2
from datetime import datetime


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print "Error"


# What are the most popular three articles of all time?
def topArticles():
    db, cursor = connect()

    query = "SELECT * FROM pageviews LIMIT 3;"

    cursor.execute(query)

    results = cursor.fetchall()

    db.close()

    return results


# How many pageviews has each author gotten?
def authorViews():
    db, cursor = connect()

    query = "SELECT * FROM authorviews;"

    cursor.execute(query)

    results = cursor.fetchall()

    db.close()

    return results


# On which days were more than 1% of pageviews errors?
def errorDays():
    db, cursor = connect()

    query = """
            SELECT *
                FROM (
                    SELECT to_char(date, 'FMMonth FMDD, YYYY'), 100.0*errors/total as percenterrors
                    FROM pageviewsverrors
                    )
                AS errors
                WHERE percenterrors >= 1;
            """

    cursor.execute(query)

    results = cursor.fetchall()

    db.close()

    return results


# Format and export report to a text file
def formatReport():
    pages = topArticles()
    authors = authorViews()
    errors = errorDays()

    f = open("report.txt", "w")

    f.write("ANALYTICS REPORT\n\nTop pages:\n")

    for i in pages:
        views = "{:,}".format(i[1])
        f.write('\"' + i[0] + '\" - ' + str(views) + " views\n")

    f.write("\n\nAuthor hits:\n")

    for i in authors:
        views = "{:,}".format(i[1])
        f.write(i[0] + " - " + str(views) + " views\n")

    f.write("\n\nErrors:\n")

    for i in errors:
        percent = round(i[1], 1)
        f.write(i[0] + " - " + str(percent) + "% errors")

formatReport()
