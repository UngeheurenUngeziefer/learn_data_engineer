USE AdventureWorks2019
SET TRANSACTION ISOLATION LEVEL
READ COMMITTED
BEGIN TRANSACTION
SELECT Name
FROM HumanResources.Department
WHERE DepartmentID = 1


-- Transaction 1
USE AdventureWorks2019;
UPDATE HumanResources.Department
SET Name = 'Non-Repeatable Read'
WHERE DepartmentID = 1;

SELECT [Name]
FROM HumanResources.Department
WHERE DepartmentID = 1
COMMIT TRANSACTION

