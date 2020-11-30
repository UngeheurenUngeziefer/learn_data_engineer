USE AdventureWorksLT2019

SELECT pc.Name as ProductCategoryName, SUM(OrderQty * UnitPrice) AS Sales
FROM SalesLT.SalesOrderDetail AS sod
INNER JOIN SalesLT.Product AS pd
ON sod.ProductID = pd.ProductID
INNER JOIN SalesLT.ProductCategory AS pc
ON pd.ProductCategoryID = pc.ProductCategoryID
GROUP BY pc.Name
ORDER BY COUNT(*) DESC

SELECT SUM(OrderQty * UnitPrice) FROM SalesLT.SalesOrderDetail