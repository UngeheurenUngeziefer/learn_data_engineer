USE AdventureWorks2019

-- divider by almost equal parts
GO
SELECT ProductID, SalesCount, NTILE(3) OVER (ORDER BY SalesCount) as Percentile
FROM (SELECT ProductID, COUNT(*) as SalesCount
FROM Sales.SalesOrderDetail
GROUP BY ProductID) AS Q
ORDER BY Percentile DESC;