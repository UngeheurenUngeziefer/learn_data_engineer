USE AdventureWorks2019

GO
ALTER PROCEDURE Sales.uspGetCurrencyInformation
WITH ENCRYPTION
AS
SELECT CurrencyCode, Name, ModifiedDate
FROM Sales.Currency
GO
