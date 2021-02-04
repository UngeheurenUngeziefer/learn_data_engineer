USE AdventureWorks2019
GO
SELECT FirstName,
       ISNULL(MiddleName, 'None') MiddleName,   -- replace MiddleName to None if is NULL
       LastName
FROM Person.Person
