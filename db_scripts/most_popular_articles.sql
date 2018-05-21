CREATE OR REPLACE VIEW MOST_POPULAR_ARTICLES_V AS
SELECT a.title  AS TITLE
      ,count(*) AS QTD_VIEWS
  FROM articles a
      ,log      l
 WHERE a.slug = SUBSTR(l.path,10)
 GROUP BY a.title 
 ORDER BY 2 DESC;
  
  