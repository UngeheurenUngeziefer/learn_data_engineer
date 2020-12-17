USE AdventureWorks2019

GO
ALTER PROCEDURE Sales.uspGetCurrencyInformation
AS
SELECT CurrencyCode, [Name], ModifiedDate
FROM Sales.Currency
GO
