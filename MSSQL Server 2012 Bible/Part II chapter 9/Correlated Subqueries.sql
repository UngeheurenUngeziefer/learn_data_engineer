USE AdventureWorksLT2019

SELECT p.ProductID, p.ProductCategoryID, p.Name
FROM SalesLT.Product p
WHERE ListPrice <
(SELECT SUM(OrderQty * UnitPrice) / Sum(sod.OrderQty) AS AveragePricePerItemInCategory
FROM SalesLT.SalesOrderDetail AS sod
INNER JOIN SalesLT.Product AS pd
ON sod.ProductID = pd.ProductID
INNER JOIN SalesLT.ProductCategory AS pc
ON pd.ProductCategoryID = pc.ProductCategoryID
WHERE pc.ProductCategoryID = p.ProductCategoryID
GROUP BY pc.Name)