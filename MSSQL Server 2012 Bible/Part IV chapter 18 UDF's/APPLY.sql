USE AdventureWorks2019

GO
SELECT t.Name, t.TotalOrders
FROM Production.Product p
CROSS APPLY dbo.ufnProductOrderTotals(p.ProductID) t
ORDER BY t.TotalOrders DESC;