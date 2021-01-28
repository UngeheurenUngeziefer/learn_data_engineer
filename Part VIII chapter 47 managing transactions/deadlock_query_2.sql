USE AdventureWorks2019
BEGIN TRANSACTION
--Step 2
UPDATE Production.Product
SET Name = 'DeadLock Repair Kit'
WHERE ProductNumber = 'FR-R38R-44'
UPDATE Person.Person
SET FirstName = 'Tim'
WHERE BusinessEntityID = 101
COMMIT TRANSACTION