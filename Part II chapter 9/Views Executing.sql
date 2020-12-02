-- using view
SELECT BusinessEntityID, LastName, FirstName, JobTitle
FROM dbo.vEmployeeList
ORDER BY BusinessEntityID

-- referencing view with filter
SELECT BusinessEntityID, LastName, FirstName, JobTitle
FROM dbo.vEmployeeList
WHERE JobTitle = 'Database Administrator'

