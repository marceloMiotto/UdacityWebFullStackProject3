import psycopg2
import db_log

#Open connection to database
conn = psycopg2.connect("dbname=news")

#Create a cursor to handle the data
cur = conn.cursor()
report = db_log.Data_Log(cur)

#Call the function to answer the first question
report.print_most_articles()

#Call the function to answer the second question
report.print_most_authors()

#Call the function to answer the third question
report.print_most_error_date()

#Close the connection
conn.close()
