CREATE OR REPLACE VIEW REQ_ERRORS_BY_DAY_V AS
SELECT TO_CHAR(a.date_total,'dd Mon YYYY') AS DATE_OF_ERROR
      ,(b.total_errors * 100) / a.total	   AS PERCENT   
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

