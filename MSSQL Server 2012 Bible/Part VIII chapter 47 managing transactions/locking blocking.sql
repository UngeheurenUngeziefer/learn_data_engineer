-- Transaction 1
USE AdventureWorks2019
BEGIN TRANSACTION
    UPDATE HumanResources.Department
    SET Name = 'New Name'
    WHERE DepartmentID = 1;


-- Transaction 2
USE AdventureWorks2019
SELECT [Name]
FROM HumanResources.Department
WHERE DepartmentID = 1;

COMMIT TRANSACTION