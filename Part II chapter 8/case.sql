USE AdventureWorks2019
GO
SELECT FirstName + ' ' + LastName AS Employee_Name,
        CASE SalariedFlag               -- comparison field
            WHEN 1 THEN 'Exempt'        -- if 1 then exempt
            WHEN 0 THEN 'NonExempt'     -- if 0 then nonexempt
        END Salary_Type                 -- name of column
FROM HumanResources.Employee e
INNER JOIN Person.Person p 
        ON e.BusinessEntityID = p.BusinessEntityID
