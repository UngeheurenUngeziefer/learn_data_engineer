USE AdventureWorks2019
GO
INSERT INTO PersonList
OUTPUT Inserted.*
VALUES(77777, 'Jane', 'Doe')