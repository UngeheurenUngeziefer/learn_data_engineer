USE AdventureWorks2019;
IF EXISTS
(
SELECT * FROM Production.ProductInventory WHERE Quantity = 0
)
BEGIN;
PRINT 'Replenish Inventory';
END;