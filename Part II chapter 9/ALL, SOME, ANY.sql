-- all values is greater than 1
SELECT 'True' AS 'AllTest'
WHERE 1 < ALL
(SELECT a
FROM (VALUES(2),(4),(5),(7),(9)) AS ValuesTable(a))

-- some of the values is equal to 5
SELECT 'True' AS 'SomeTest'
WHERE 5 = SOME
(SELECT a
FROM (VALUES(2), (3), (5), (7), (9)) AS MyTable(a))

-- any of the values is equal to 3
SELECT 'True' AS 'TestColumn'
WHERE 3 = ANY
(SELECT a
FROM (VALUES(2), (3), (5), (7), (9)) AS MyTable(a))
