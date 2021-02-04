USE AdventureWorks2019

GO
CREATE FUNCTION dbo.ufnGetProductsAndOrderTotals()
RETURNS @ProductList TABLE
(
    ProductID int,
    ProductName nvarchar(100),
    TotalOrders int
)
AS
BEGIN
    INSERT @ProductList(ProductID, ProductName)
    SELECT ProductID, [Name]
    FROM Production.Product
    UPDATE pl
    SET TotalOrders =
        (
            SELECT sum(sod.OrderQty)
            FROM @ProductList ipl
            JOIN Sales.SalesOrderDetail sod
            ON ipl.ProductID = sod.ProductID
            WHERE ipl.ProductID = pl.ProductID
        )
    FROM @ProductList pl
    RETURN
END

GO
SELECT ProductID, ProductName, TotalOrders
FROM dbo.ufnGetProductsAndOrderTotals()
ORDER BY TotalOrders DESC;