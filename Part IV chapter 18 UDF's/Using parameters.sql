CREATE VIEW dbo.vwProductOrderTotals                            -- создаём представление
AS
SELECT p.ProductID, p.Name, sum(sod.OrderQty) as TotalOrders
FROM Production.Product p
JOIN Sales.SalesOrderDetail sod
    ON p.ProductID = sod.ProductID
GROUP BY p.ProductID, p.Name

GO
SELECT *                                                        -- возвращаем значения
FROM dbo.vwProductOrderTotals
WHERE ProductID = 782                                           -- с id 782
