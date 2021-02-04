USE AdventureWorks2019
UPDATE Person.Person                            -- updates one of the rows to a blank for testing purposes
SET MiddleName = ''
    WHERE LastName = 'Abbas'
SELECT LastName, FirstName,
    CASE MiddleName
        WHEN '' THEN 'blank'                    -- varchar blank
        ELSE MiddleName
    END AS MiddleName,
    NULLIF(MiddleName, '') as MiddleNameNullIf  -- NULL
FROM Person.Person
WHERE LastName IN ('Abbas', 'Abel')
ORDER BY LastName, FirstName;
