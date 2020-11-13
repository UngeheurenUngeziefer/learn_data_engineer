USE AdventureWorks2019
SELECT TOP(6) WITH TIES
    ProductNumber, Name, ListPrice,
    CONVERT(VARCHAR(10), SellStartDate, 1) SellStartDate
FROM Production.Product
ORDER BY ListPrice DESC