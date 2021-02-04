USE AdventureWorks2019
GO
SELECT FirstName, MiddleName, LastName
FROM Person.Person
WHERE
    MiddleName IS NOT NULL
ORDER BY LastName, FirstName