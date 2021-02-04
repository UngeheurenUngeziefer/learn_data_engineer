USE AdventureWorks2019

GO
SELECT definition
FROM sys.sql_modules
WHERE object_id = 
    (
        OBJECT_ID
        (N'Sales.uspGetCurrencyInformation')
    )
