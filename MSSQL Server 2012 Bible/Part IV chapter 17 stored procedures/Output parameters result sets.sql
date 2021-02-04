USE AdventureWorks2019
DROP PROCEDURE Sales.uspGetCurrencyInfoAndDetail
GO
CREATE PROCEDURE Sales.uspGetCurrencyInfoAndDetail          -- создаём процедуру
    @CurrencyCode char(3),
    @CurrencyRateDate date
AS
SELECT CurrencyCode, [Name]
FROM Sales.Currency
WHERE CurrencyCode = @CurrencyCode
SELECT FromCurrencyCode, ToCurrencyCode,
        AverageRate, EndOfDayRate, CurrencyRateDate
FROM Sales.CurrencyRate
WHERE FromCurrencyCode = @CurrencyCode
AND CurrencyRateDate = @CurrencyRateDate

GO
EXECUTE Sales.uspGetCurrencyInfoAndDetail
    @CurrencyCode = 'USD',
    @CurrencyRateDate = '2014-01-11'
WITH RESULT SETS
(
    ( 
      [Currency Code] char(3),
      [Currency Name] varchar(50)
    ),                                                      -- Разделяем запятой каждый набор результатов
    
    ( 
     [From Currency] char(3),
     [To Currency] char(3),
     [Average Rate] numeric(7,4),
     [End of Day Rate] numeric(7,4),
     [Currency As-Of Date] date
    )
)
