USE AdventureWorks2019
SELECT TOP(6)
    ProductNumber, Name, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC