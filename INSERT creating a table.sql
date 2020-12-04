USE AdventureWorks2019

-- sample code for setting the bulk-logged behavior
ALTER DATABASE AdventureWorks2019 SET RECOVERY BULK_LOGGED;

-- the select/into statement
GO
SELECT BusinessEntityID, LastName, FirstName
INTO PersonList
FROM Person.Person
ORDER BY LastName, FirstName

INSERT PersonList (BusinessEntityID, LastName, FirstName)
VALUES(99999,'LeBlanc', 'Patrick');


SELECT TOP(10) *
FROM PersonList