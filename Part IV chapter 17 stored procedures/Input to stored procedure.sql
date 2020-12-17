USE AdventureWorks2019

DROP PROCEDURE Sales.uspGetCurrencyInformation

GO
CREATE PROCEDURE Sales.uspGetCurrencyInformation
@CurrencyCode char(3)
AS
SELECT CurrencyCode, Name
FROM Sales.Currency
WHERE CurrencyCode = @CurrencyCode

GO
EXECUTE Sales.uspGetCurrencyInformation 'USD'

GO
ALTER PROCEDURE Sales.uspGetCurrencyInformation
@CurrencyCode char(3) = 'USD'
AS
SELECT CurrencyCode, Name
FROM Sales.Currency
WHERE CurrencyCode = @CurrencyCode;

GO
EXECUTE Sales.uspGetCurrencyInformation
EXECUTE Sales.uspGetCurrencyInformation DEFAULT



