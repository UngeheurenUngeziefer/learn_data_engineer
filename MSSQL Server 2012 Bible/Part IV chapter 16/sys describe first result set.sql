SELECT *
FROM sys.dm_exec_describe_first_result_set
(N'TSQL', N'Parameters', 0);


USE AdventureWorks2019
GO
SELECT *
FROM sys.dm_exec_describe_first_result_set
(N'SELECT c.Name, s.Name, p.Name
FROM Production.ProductCategory c
JOIN Production.ProductSubcategory s
ON c.ProductCategoryID = s.ProductCategoryID
JOIN Production.Product p
ON s.ProductSubcategoryID = p.ProductSubcategoryID
WHERE c.ProductCategoryID = @ProductCategoryID',
N'@ProductCategoryID int',
0);