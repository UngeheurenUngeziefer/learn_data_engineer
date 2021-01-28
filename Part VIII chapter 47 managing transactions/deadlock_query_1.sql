USE AdventureWorks2019
BEGIN TRANSACTION
--Step 1
UPDATE Person.Person
SET LastName = 'Chapman'
WHERE BusinessEntityID = '101'

--Step 3
UPDATE Production.Product
SET Name = 'DeadLock Identification Tester'
WHERE ProductNumber = 'FR-R38R-44'
COMMIT TRANSACTION


