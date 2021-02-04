USE AdventureWorks2019

GO
SELECT OBJECT_DEFINITION 
    (OBJECT_ID
        (N'AdventureWorks2019.Sales.uspGetCurrencyInformation')
    );
