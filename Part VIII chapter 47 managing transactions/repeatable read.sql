SET TRANSACTION ISOLATION LEVEL
REPEATABLE READ
BEGIN TRANSACTION;
SELECT Name
FROM HumanResources.Department
WHERE DepartmentID = 1

-- Transaction 1
USE AdventureWorks2019
UPDATE HumanResources.Department
SET Name = 'Non-Repeatable Read'
WHERE DepartmentID = 1

SELECT [Name]
FROM HumanResources.Department
WHERE DepartmentID = 1