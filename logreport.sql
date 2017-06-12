
-- summarize pageviews per article
CREATE VIEW pageviews AS
    SELECT Articles.title, count(Log.path) as views
    FROM Articles JOIN Log
    ON '/article/' || Articles.slug = Log.path
    GROUP BY Articles.title
    ORDER BY views desc;


-- summarize pageviews per author
CREATE VIEW authorviews AS
    SELECT Authors.name, count(Log.path) as views
    FROM Articles, Log, Authors
    WHERE Authors.id = Articles.author
        AND '/article/' || Articles.slug = Log.path
    GROUP BY Authors.name
    ORDER BY views desc;



--Errors
CREATE VIEW pageviewsverrors AS
    SELECT Log.time::date,
           count(*) FILTER (WHERE status = '200 OK') as success,
           count(*) FILTER (WHERE status = '404 NOT FOUND') as errors
        FROM Log
        GROUP BY Log.time::date
        ORDER BY success desc;


CREATE VIEW errors AS
    SELECT *
        FROM (
            SELECT time, 100.0*errors/(errors+success) as percenterrors
            FROM pageviewsverrors
            )
        AS errors
        WHERE percenterrors >= 1
        ORDER BY percenterrors desc;

-- errors per day
-- count