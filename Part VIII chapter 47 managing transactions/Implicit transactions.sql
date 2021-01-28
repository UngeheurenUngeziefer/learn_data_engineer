USE AdventureWorks2019

SET Implicit_Transactions ON;

UPDATE HumanResources.Department
SET Name = 'Department of Redundant Departments'
WHERE DepartmentID = 2;

SELECT @@TRANCOUNT AS PendingTransactions; -- one pending transaction level awaiting a commit or rollback

COMMIT TRANSACTION;

SET Implicit_Transactions OFF;