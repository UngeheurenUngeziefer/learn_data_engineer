-- concatenation of word + column values
USE AdventureWorks2019
GO
SELECT 'Product: ' + Name AS Product
FROM Production.Product