-- update a record
USE AdventureWorks2019
UPDATE dbo.Address
SET Address1 = '1970 Napa Court'
WHERE AddressID = 1

-- show the table
SELECT AddressID, Address1
FROM dbo.Address
WHERE AddressID = 1;