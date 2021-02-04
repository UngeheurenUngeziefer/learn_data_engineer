CREATE TABLE #ProductTemp (
ProductID INT PRIMARY KEY
);


SELECT name
FROM tempdb.sys.objects
WHERE name LIKE '#Pro%';


SELECT * 
FROM #ProductTemp