CREATE FUNCTION dbo.ufnProductOrderTotals (@ProductID nvarchar(100))        -- создаём функцию
RETURNS TABLE
AS
RETURN
(
    SELECT p.ProductID, p.Name, sum(sod.OrderQty) as TotalOrders
    FROM Production.Product p
    JOIN Sales.SalesOrderDetail sod
    ON p.ProductID = sod.ProductID
    WHERE p.ProductID = @ProductID
    GROUP BY p.ProductID, p.Name
)

GO                                                                          -- CROSS APPLY применяет
SELECT t.Name, t.TotalOrders                                                -- функцию к каждой строке
FROM Production.Product p
CROSS APPLY dbo.ufnProductOrderTotals(p.ProductID) t
ORDER BY t.TotalOrders DESC
