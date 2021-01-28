-- Transaction 2
USE AdventureWorks2019
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ
BEGIN TRANSACTION
SELECT DepartmentID as DeptID, Name
FROM HumanResources.Department
WHERE Name BETWEEN 'A' AND 'G'

-- Transaction 1 now inserts a new row into the range selected by transaction 2:
-- Transaction 1
-- Insert a row in the range
INSERT HumanResources.Department (Name, GroupName)
VALUES ('ABC Dept', 'Test Dept')

-- When transaction 2 selects the same range again, if ‘ABC Dept’ is in the result list, then a
-- phantom row transaction fault occurred:
-- Transaction 2
SELECT DepartmentID as DeptID, Name
FROM HumanResources.Department
WHERE Name BETWEEN 'A' AND 'G'
COMMIT TRANSACTION