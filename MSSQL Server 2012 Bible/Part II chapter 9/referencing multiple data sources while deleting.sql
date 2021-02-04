USE AdventureWorks2019

SELECT *
INTO dbo.Product
FROM Production.Product

DELETE dbo.Product
FROM dbo.Product p
INNER JOIN Production.ProductSubcategory s
ON p.ProductSubcategoryID = s.ProductSubcategoryID
WHERE s.Name = 'Jerseys'


DELETE FROM dbo.Product
WHERE EXISTS
    (SELECT *
    FROM Production.ProductSubcategory AS ps
    WHERE ps.ProductSubcategoryID = Product.ProductSubcategoryID
    AND ps.Name = 'Jerseys')