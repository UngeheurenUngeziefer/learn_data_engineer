USE AdventureWorks2019
GO

-- Ancient way
SELECT *
FROM Sales.SalesOrderDetail sod, Production.Product p
WHERE p.ProductID = sod.ProductID
GO

-- The ANSI way
SELECT *
FROM Sales.SalesOrderDetail sod
LEFT JOIN Production.Product p
	   ON p.ProductID = sod.ProductID
GO
