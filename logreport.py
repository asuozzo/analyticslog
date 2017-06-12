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


# 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
# note: Log.path = "/article/" + Articles.slug


def topArticles():
    db, cursor = connect()

    query = "SELECT * FROM pageviews LIMIT 3;"

    cursor.execute(query)

    results = cursor.fetchall()

    db.close()

    return results

# 2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
def authorViews():
    db, cursor = connect()

    query = "SELECT * FROM authorviews;"

    cursor.execute(query)

    results = cursor.fetchall()

    db.close()

    return results

# 3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer back to this lesson if you want to review the idea of HTTP status codes.)
def errorDays():
    db, cursor = connect()

    query = "SELECT * FROM errors;"

    cursor.execute(query)

    results = cursor.fetchall()

    db.close()

    return results


# Create summary report
def formatReport():
    pages = topArticles()
    authors = authorViews()
    errors = errorDays()

    f = open("report.txt","w")

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
        date = datetime.strftime(i[0],'%B %d, %Y')
        percent = round(i[1],1)
        f.write(str(date) + " - " + str(percent) + "% errors")

formatReport()






