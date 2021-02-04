USE AdventureWorks2019
SELECT Description, LEN(Description) AS TextLength
FROM Production.ProductDescription
WHERE
    Description LIKE 'Replacement%'
ORDER BY 
CASE 
    WHEN LEFT(Description, 5) = 'This '
    THEN Stuff(Description, 1, 5, '')
ELSE
    DESCRIPTION
END