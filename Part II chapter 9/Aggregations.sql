USE AdventureWorks2019;
SELECT COUNT(*),
       SUM(TotalDue) AS [SUM],
       AVG(TotalDue) AS [AVG],
       MIN(TotalDue) AS [MIN],
       MAX(TotalDue) AS [MAX]
FROM Sales.SalesOrderHeader