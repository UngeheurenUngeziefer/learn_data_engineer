USE AdventureWorks2019;
GO 
UPDATE HumanResources.Department
SET Name = 'Ministry of Silly Walks'
WHERE DepartmentID = 100;
IF @@rowCount = 0
BEGIN
-- error handling code
PRINT 'no rows affected'
END;