USE AdventureWorks2019
SELECT TOP(3) PERCENT
    ProductNumber, Name, ListPrice, SellStartDate
FROM Production.Product
ORDER BY ListPrice DESC