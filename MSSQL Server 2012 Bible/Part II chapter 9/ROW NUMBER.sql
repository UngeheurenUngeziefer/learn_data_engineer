USE AdventureWorks2019

GO
WITH Results AS
(SELECT ROW_NUMBER()
    OVER(ORDER BY PurchaseOrderID, ShipDate) AS RowNumber,
    PurchaseOrderID,
    ShipDate
FROM Purchasing.PurchaseOrderHeader)

SELECT *
FROM Results
WHERE RowNumber BETWEEN 21 AND 40


GO
SELECT ROW_NUMBER()
    OVER(ORDER BY PurchaseOrderID, ShipDate) AS RowNumber,
    PurchaseOrderID,
    ShipDate
FROM Purchasing.PurchaseOrderHeader
ORDER BY RowNumber
OFFSET 20 ROWS
FETCH NEXT 20 ROWS ONLY


