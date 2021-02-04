DELETE FROM Production.ProductSubcategory
WHERE Name = 'Bike Pedal';
GO
USE AdventureWorks2008R2
GO
ALTER view vComponentsProductSubCats
AS
SELECT
ProductCategoryID,
Name ProductSubCategory
FROM Production.ProductSubcategory
WHERE ProductCategoryID = 1;
WITH CHECK OPTION;
go
INSERT INTO vComponentsProductSubCats(ProductCategoryID,
ProductSubCategory)
VALUES(2, 'Bike Pedal');