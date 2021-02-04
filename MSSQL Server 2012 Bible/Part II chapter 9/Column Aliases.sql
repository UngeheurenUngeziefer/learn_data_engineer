-- creating an aliases for column names
ALTER VIEW dbo.vEmployeeList
(ID, Last, First, Job)
AS
SELECT P.BusinessEntityID, P.LastName, P.FirstName,
	   E.JobTitle
FROM Person.Person P
INNER JOIN HumanResources.Employee E
ON P.BusinessEntityID = E.BusinessEntityID

GO

SELECT *
FROM dbo.vEmployeeList
ORDER BY ID

