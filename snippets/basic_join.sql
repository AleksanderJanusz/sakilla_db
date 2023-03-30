CREATE  table table1(
    ID INT, Value VARCHAR(10)
);

CREATE  table table2(
    ID INT, Value VARCHAR(10)
);

INSERT INTO table1 (ID, Value)
VALUES (1, 'First'),
       (2, 'Second'),
       (3, 'Third'),
       (4, 'Fourth'),
       (5, 'Fifth');


INSERT INTO table2 (ID, Value)
VALUES (1, 'First'),
       (2, 'Second'),
       (3, 'Third'),
       (6, 'Sixth'),
       (7, 'Seventh'),
       (8, 'Eighth');

SELECT *
FROM table1;

SELECT *
FROM table2;

SELECT *
FROM table1 t1
INNER JOIN table2 t2 ON t1.ID = t2.ID;

SELECT t1.ID AS t1ID, t2.ID AS t2ID, t1.Value AS t1Value, t2.Value AS t2Value
FROM table1 t1
INNER JOIN table2 t2 ON t1.ID = t2.ID;

SELECT *
FROM table1 t1
LEFT JOIN table2 t2 ON t1.ID = t2.ID;

SELECT *
FROM table1 t1
RIGHT JOIN table2 t2 ON t1.ID = t2.ID;

SELECT *
FROM table1 t1
FULL JOIN table2 t2 ON t1.ID = t2.ID;


SELECT *
FROM table1 t1
RIGHT JOIN table2 t2 ON t1.ID = t2.ID
WHERE  t1.ID IS NULL;

SELECT *
FROM table1 t1
CROSS JOIN table2 t2;
