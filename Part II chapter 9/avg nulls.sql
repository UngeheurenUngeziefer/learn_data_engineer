USE AdventureWorks2019
ALTER TABLE Sales.SalesPersonQuotaHistory
ALTER COLUMN SalesQuota money null
GO
UPDATE Sales.SalesPersonQuotaHistory
SET SalesQuota = NULL
WHERE BusinessEntityID = 274
AND QuotaDate = '2005-07-01 00:00:00.000'
SELECT
AVG(SalesQuota) AS [Avg Function],
SUM(SalesQuota) / COUNT(*) AS [Manual AVG]
FROM Sales.SalesPersonQuotaHistory