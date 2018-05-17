CREATE OR REPLACE VIEW MOST_POPULAR_AUTHORS_V AS
SELECT au.name                         AS NAME
      ,to_char(count(*),'99999999990') AS QTD_VIEWS
  FROM authors  au
      ,articles ar
      ,log      lo
 WHERE au.id   = ar.author
   and ar.slug = SUBSTR(lo.path,10)
 GROUP BY au.name
 ORDER BY 2 DESC;
  
  