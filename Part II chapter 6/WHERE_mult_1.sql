USE AdventureWorks2019
SELECT ProductID, Name
FROM Production.Product
WHERE
    Name LIKE 'Chain%'
OR
    ProductID BETWEEN 320 AND 324
AND
    Name Like '%s%';