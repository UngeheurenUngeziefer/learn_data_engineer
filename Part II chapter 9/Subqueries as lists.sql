SELECT FirstName, LastName
FROM dbo.Contact
WHERE Region IN (Subquery that returns a list of states);