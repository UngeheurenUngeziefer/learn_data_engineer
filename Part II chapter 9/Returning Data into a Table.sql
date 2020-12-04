USE AdventureWorks2019

DECLARE @DeletedPerson TABLE (
    BusinessEntityID INT NOT NULL PRIMARY KEY,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);

DELETE dbo.PersonList
OUTPUT Deleted.BusinessEntityID, Deleted.LastName, Deleted.FirstName
INTO @DeletedPerson
WHERE BusinessEntityID = 2;


SELECT BusinessEntityID, LastName, FirstName FROM @DeletedPerson;