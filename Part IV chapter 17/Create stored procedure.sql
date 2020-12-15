USE AdventureWorks2019

GO
CREATE PROCEDURE Sales.uspGetCurrencyInformation
AS
SELECT CurrencyCode, [Name]
FROM Sales.Currency
