USE AdventureWorks2019
GO
CREATE VIEW dbo.vEmployeeList AS
SELECT P.BusinessEntityID, P.Title, P.LastName, P.FirstName, E.JobTitle
FROM Person.Person P
INNER JOIN HumanResources.Employee E
ON P.BusinessEntityID = E.BusinessEntityID


SELECT BusinessEntityID, LastName, FirstName, JobTitle
FROM dbo.vEmployeeList
ORDER BY BusinessEntityID


SELECT BusinessEntityID, LastName, FirstName, JobTitle
FROM dbo.vEmployeeList
WHERE JobTitle = 'Database Administrator';


SELECT *
FROM dbo.vEmployeeList
ORDER BY LastName, FirstName

