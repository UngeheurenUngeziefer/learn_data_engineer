USE AdventureWorks2019
SELECT LastName + ' ' + FirstName AS FullName
FROM Person.Person
ORDER BY LastName + ', ' + FirstName