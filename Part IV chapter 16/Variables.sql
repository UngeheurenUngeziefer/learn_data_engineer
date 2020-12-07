USE AdventureWorks2019
DECLARE @ProductID int = 999;
SELECT Name
FROM Production.Product
WHERE ProductID = @ProductID;