--Transaction 1
USE AdventureWorks2019

BEGIN TRANSACTION                                       -- tran 1 hasn't yet commited
UPDATE HumanResources.Department
SET Name = 'Transaction Fault'
WHERE DepartmentID = 1

-- Transaction 2
USE AdventureWorks2019;                                 -- but this tran read tran 1
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT Name
FROM HumanResources.Department
WHERE DepartmentID = 1;