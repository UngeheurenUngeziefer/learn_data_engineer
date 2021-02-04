--From Subquery [AS] Alias
USE AdventureWorks2019
SELECT SQL.LastName, SQL.FirstName
FROM (SELECT LastName, FirstName from Person.Person) AS SQL;