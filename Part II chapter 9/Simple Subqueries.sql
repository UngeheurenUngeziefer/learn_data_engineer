SELECT (SELECT 3) AS SubqueryValue;

SELECT 3 AS SubqueryValue;

USE AdventureWorksLT2019;
SELECT pd.Name as ProductName
FROM SalesLT.Product pd
WHERE ProductCategoryID IN (SELECT ProductCategoryID
                            FROM SalesLT.ProductCategory
                            WHERE Name = 'Cranksets')


SELECT ProductCategoryID
FROM SalesLT.ProductCategory
WHERE Name = 'Cranksets'


SELECT Name as ProductName
FROM SalesLT.Product
WHERE ProductCategoryID = 12