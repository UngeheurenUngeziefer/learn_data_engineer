USE AdventureWorks2019
UPDATE Person.Person WITH(ROWLOCK)
SET LastName = 'Chapman'
WHERE BusinessEntityID = 1

SELECT LastName
FROM Person.Person
WHERE BusinessEntityID = 1