import psycopg2

class Data_Log():
    def __init__(self, cursor):
        self.cursor = cursor                

    def print_most_articles(self):
        self.cursor.execute("SELECT * FROM most_popular_articles_v limit 3")
        results = self.cursor.fetchall()
        print "Title     ->     Views"
        for title, qtd_views in results:
            print title + " -> " + str(qtd_views)
        print " "
        print "------------------------------------------------------------"

    def print_most_authors(self):
        self.cursor.execute("SELECT * FROM most_popular_authors_v")
        results = self.cursor.fetchall()
        print "Name     ->     Views"
        for name, qtd_views in results:
            print name + " -> " + str(qtd_views)
        print " "
        print "------------------------------------------------------------"

    def print_most_error_date(self):
        self.cursor.execute("SELECT * FROM req_errors_by_day_v")
        results = self.cursor.fetchall()
        print "Date     ->     Percentage"
        for date_of_error, percent in results:
            if percent > 1:
                print date_of_error + " -> " + str(percent) + "%"
        print " "
        print "------------------------------------------------------------"        




