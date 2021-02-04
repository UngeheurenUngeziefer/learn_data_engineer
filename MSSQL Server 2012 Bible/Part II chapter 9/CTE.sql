USE AdventureWorksLT2019

WITH CTEQuery (ProductCategoryID) AS 
(SELECT ProductCategoryID
 FROM SalesLT.ProductCategory
 WHERE Name = 'Cranksets')

SELECT Name AS ProductName
FROM SalesLT.Product p
INNER JOIN CTEQuery c
ON p.ProductCategoryID = c.ProductCategoryID;