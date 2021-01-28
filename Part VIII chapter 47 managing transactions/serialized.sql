-- Transaction 2
USE AdventureWorks2019
-- insert test row for deletion
INSERT HumanResources.Department
(Name, GroupName)
VALUES ('Amazing FX Dept', 'Test Dept')
SET TRANSACTION ISOLATION LEVEL
SERIALIZABLE
BEGIN TRANSACTION
SELECT DepartmentID as DeptID, Name
FROM HumanResources.Department
WHERE Name BETWEEN 'A' AND 'G'


-- Transaction 1
-- Insert a row in the range
INSERT HumanResources.Department (Name, GroupName)
VALUES ('ABC Dept', 'Test Dept')
-- Update Dept into the range
UPDATE HumanResources.Department
SET Name = 'ABC Test'
WHERE DepartmentID = 1 -- Engineering
-- Delete Dept from range
DELETE HumanResources.Department
WHERE DepartmentID = 17 -- Amazing FX Dept


-- Transaction 2 now reselects the same range:
SELECT DepartmentID as DeptID, Name
FROM HumanResources.Department
WHERE Name BETWEEN 'A' AND 'G'

COMMIT TRANSACTION

SELECT *
FROM HumanResources.Department