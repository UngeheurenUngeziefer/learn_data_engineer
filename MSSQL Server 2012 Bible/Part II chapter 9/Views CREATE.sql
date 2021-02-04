USE AdventureWorks2019
GO

-- creating a view
CREATE VIEW dbo.vEmployeeList
AS
SELECT P.BusinessEntityID, P.Title, P.LastName,
	   P.FirstName, E.JobTitle
FROM Person.Person P
INNER JOIN HumanResources.Employee E
ON P.BusinessEntityID = E.BusinessEntityID