USE AdventureWorks2019

SELECT ProductID, Product, SalesCount,
       NTILE(100) OVER (ORDER BY SalesCount) as Percentile, 
       SubCat,
       CAST(CAST(SalesCount AS NUMERIC(9,2))
        / SUM(SalesCount) OVER(Partition BY SubCat) 
        * 100 AS NUMERIC (4,1)) AS SubPer
FROM (SELECT P.ProductID,
             P.[Name] AS Product,
             PSC.Name AS SubCat, 
             COUNT(*) as SalesCount
    FROM Sales.SalesOrderDetail AS SOD
    JOIN Production.Product AS P
    ON SOD.ProductID = P.ProductID
    JOIN Production.ProductSubcategory PSC
    ON P.ProductSubcategoryID = PSC.ProductSubcategoryID
    GROUP BY PSC.Name, P.[Name], P.ProductID) Q
ORDER BY Percentile DESC


SELECT CAST(25.65 AS int)
