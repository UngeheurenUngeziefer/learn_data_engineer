USE AdventureWorks2019
SELECT DISTINCT p.Name
FROM Production.Product AS p
INNER JOIN Sales.SalesOrderDetail sod
        ON p.ProductID = sod.ProductID