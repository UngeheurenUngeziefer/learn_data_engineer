USE AdventureWorks2019
GO
DECLARE @ProductID int,
        @ProductName varchar(25);
SET @ProductID = 782;
SELECT @ProductID = ProductID,
       @ProductName = Name
FROM Production.Product
ORDER BY ProductID;
SELECT @ProductID as ProductID, @ProductName as ProductName;
