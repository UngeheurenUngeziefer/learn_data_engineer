USE AdventureWorks2019
UPDATE PersonList
SET FirstName = 'Jane', LastName = 'Doe'
OUTPUT Deleted.FirstName OldFirstName,
       Deleted.LastName OldLastName,
       Inserted.FirstName NewFirstName,
       Inserted.LastName NewLastName
WHERE BusinessEntityID = 77777