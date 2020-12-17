GO
CREATE FUNCTION                                                     -- создаём таблично значимую функцию
dbo.ufnGetOrderTotalByProductCategory(@ProductCategoryID int)
RETURNS TABLE                                                       -- которая будет возвращать таблицу
AS
RETURN
(
    SELECT p.ProductID, p.Name, sum(sod.OrderQty) as TotalOrders
    FROM Production.Product p
    JOIN Sales.SalesOrderDetail sod
        ON p.ProductID = sod.ProductID
    JOIN Production.ProductSubcategory s
        ON p.ProductSubcategoryID = s.ProductSubcategoryID
    JOIN Production.ProductCategory c
        ON s.ProductCategoryID = c.ProductCategoryID
    WHERE c.ProductCategoryID = @ProductCategoryID
    GROUP BY p.ProductID, p.Name
)

GO
SELECT ProductID, Name, TotalOrders
FROM dbo.ufnGetOrderTotalByProductCategory(1)       -- вызываем функцию с параметром id 1
ORDER BY TotalOrders DESC
