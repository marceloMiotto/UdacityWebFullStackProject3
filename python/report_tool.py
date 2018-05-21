#!/usr/bin/env python para Python 2
import psycopg2
import db_log


def connect(database_name):
    """Connect to the database.  Returns a database connection."""
    try:
        db = psycopg2.connect(dbname=database_name)
        return db

    except psycopg2.Error as e:
        # THEN you could print an error
        # and perhaps exit the program
        print (\"Unable to connect to database\")
        sys.exit(1)


# Open connection to database
conn = connect("news")

# Create a cursor to handle the data
cur = conn.cursor()
report = db_log.Data_Log(cur)

# Call the function to answer the first question
report.print_most_articles()

# Call the function to answer the second question
report.print_most_authors()

# Call the function to answer the third question
report.print_most_error_date()

# Close the connection
conn.close()
