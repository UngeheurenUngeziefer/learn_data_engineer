USE AdventureWorksLT2019

SELECT P1.Name,
       a.ProductID ,
       a.ProductTotal ,
       a.ModifiedDate
FROM SalesLT.Product p1
JOIN 
(SELECT sod.ProductID, SUM(sod.LineTotal) AS 'ProductTotal', sod.ModifiedDate
FROM SalesLT.SalesOrderDetail sod
JOIN SalesLT.Product p
ON sod.ProductID = p.ProductID
JOIN SalesLT.ProductCategory pc
ON p.ProductCategoryID = pc.ProductCategoryID
WHERE pc.Name = 'Vests'
GROUP BY sod.ProductID, sod.ModifiedDate) a
ON p1.ProductID = a.ProductID