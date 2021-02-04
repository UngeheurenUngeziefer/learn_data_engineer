USE AdventureWorks2019
DECLARE @ErrorNumber nvarchar(1000);
UPDATE HumanResources.Employee
SET BusinessEntityID = 30000
WHERE BusinessEntityID = 2;
SET @ErrorNumber = @@Error
PRINT @@error;
PRINT @ErrorNumber;