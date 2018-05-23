import psycopg2

class Data_Log():
    def __init__(self, cursor):
        self.cursor = cursor                

    def print_most_articles(self):
        self.cursor.execute("SELECT * FROM most_popular_articles_v limit 3")
        results = self.cursor.fetchall()
        print "1. What are the three most popular articles of all time? "
        print " "
        for title, qtd_views in results:
            print "    " + title + " -> " + str(qtd_views) + " views"
        print " "
        print "------------------------------------------------------------"

    def print_most_authors(self):
        self.cursor.execute("SELECT * FROM most_popular_authors_v")
        results = self.cursor.fetchall()
        print "2. Who are the authors of most popular articles of all time?"
        print " "
        for name, qtd_views in results:
            print "    " + name + " -> " + str(qtd_views) + " views"
        print " "
        print "------------------------------------------------------------"

    def print_most_error_date(self):
        self.cursor.execute("SELECT * FROM req_errors_by_day_v")
        results = self.cursor.fetchall()
        print "3. On what days more than 1% of requests resulted in errors?"
        print " "
        for date_of_error, percent in results:
            if percent > 1:
                print "    " + date_of_error + " -> " + str(percent) + "% errors"
        print " "
        print "------------------------------------------------------------"        




