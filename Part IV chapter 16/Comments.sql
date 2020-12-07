USE AdventureWorks2019
SELECT Name, ProductID   -- selects the columns
FROM Production.Product  -- the source table
WHERE Name LIKE 'Hex%';  -- the row restriction

/*
Product Table INSERT
Version 1.0
May 15, 2012
*/