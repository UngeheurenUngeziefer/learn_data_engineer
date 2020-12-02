CREATE VIEW dbo.EmployeeListDBA
AS
SELECT BusinessEntityID, LastName, FirstName, JobTitle
FROM dbo.vEmployeeList AS vE
WHERE JobTitle = 'Database Administrator'