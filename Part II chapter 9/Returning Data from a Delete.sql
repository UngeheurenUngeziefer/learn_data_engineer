USE AdventureWorks2019
GO
DELETE FROM PersonList
OUTPUT DELETED.*
WHERE BusinessEntityID = 77777

SELECT *
FROM PersonList
WHERE BusinessEntityID > 77776