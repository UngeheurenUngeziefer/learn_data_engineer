USE AdventureWorks2019
SELECT ALL p.Name
FROM Production.Product AS p
INNER JOIN Sales.SalesOrderDetail sod
        ON p.ProductID = sod.ProductID