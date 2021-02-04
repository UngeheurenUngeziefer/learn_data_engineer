USE AdventureWorks2019
GO
CREATE view vComponentsProductSubCats
AS
SELECT
ProductCategoryID,
Name ProductSubCategory
FROM Production.ProductSubcategory
WHERE ProductCategoryID = 1;
GO
SELECT ProductCategoryID, ProductSubCategory 
FROM dbo.vComponentsProductSubCats

-- insertion, disappearing rows
INSERT INTO vComponentsProductSubCats(ProductCategoryID,
ProductSubCategory)
VALUES(2, 'Bike Pedal');