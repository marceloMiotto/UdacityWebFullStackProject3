# Udacity Web FullStack Project3
Third project at Udacity Nanodegree Web FullStack.
This project was written in Python and Psql, the final result is a report from the database logs. 



# How to use
    1 - Download the project
    2 - You'll need the Virtual Machine from past lessons (You can download the Vagrant from this link https://www.vagrantup.com/downloads.html)
    3 - Put the files inside the vagrant directory
    4 - How to access the VM
        4.1 - Open the git bash on the directory where you install the VM
        4.2 - Use the command "vagrant ssh" to login into Linux
        4.3 - Open the postgres console with command "psql -d news" 
    5 - Create 3 views for this project
        5.1 - The view with the most popular articles
              CREATE OR REPLACE VIEW MOST_POPULAR_ARTICLES_V AS
                  SELECT a.title  AS TITLE
                        ,count(*) AS QTD_VIEWS
                    FROM articles a
                        ,log      l
                   WHERE a.slug = SUBSTR(l.path,10)
                   GROUP BY a.title 
                   ORDER BY 2 DESC;
  

        5.2 - The view with the most popular authors
              CREATE OR REPLACE VIEW MOST_POPULAR_AUTHORS_V AS
                  SELECT au.name       AS NAME
                        ,count(*)      AS QTD_VIEWS
                    FROM authors  au
                        ,articles ar
                        ,log      lo
                   WHERE au.id   = ar.author
                     AND ar.slug = SUBSTR(lo.path,10)
                   GROUP BY au.name
                   ORDER BY 2 DESC;

        5.3 - The view with the days and the percentual errors
              CREATE OR REPLACE VIEW REQ_ERRORS_BY_DAY_V AS
                 SELECT TO_CHAR(a.date_total,'dd Mon YYYY') AS DATE_OF_ERROR
                       ,(b.total_errors * 100) / a.total    AS PERCENT   
                   FROM (SELECT DATE(time) AS date_total 
                               ,COUNT(*)  AS total
                           FROM log lo
                          GROUP BY DATE(time)
                        ) a 
                       ,(SELECT DATE(time) AS date_error 
                               ,COUNT(*)  AS total_errors
                           FROM log
                          WHERE status     = '404 NOT FOUND'           
                          GROUP BY DATE(time)
                        ) b
                  WHERE a.date_total = b.date_error

    6 - Execute the "report_tool.py" file from python directory. (eg. python report_tool)
    7 - The scripts to create the views you can find inside the directory "db_scripts"
