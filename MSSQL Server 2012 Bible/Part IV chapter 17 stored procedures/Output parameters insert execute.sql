USE AdventureWorks2019
DROP TABLE Sales.NewCurrency
DROP PROCEDURE Sales.uspInsertNewCurrency

GO
CREATE TABLE Sales.NewCurrency                                  -- Создаём таблицу
(   
    CurrencyCode char(3),
    Name varchar(50)
)

GO
CREATE PROCEDURE Sales.uspInsertNewCurrency                     -- Создаём процедуру
    @CurrencyCode char(3)
AS
SELECT CurrencyCode, Name
FROM Sales.Currency
WHERE CurrencyCode = @CurrencyCode

GO
INSERT Sales.NewCurrency(CurrencyCode, Name)                    -- INSERT... EXECUTE в Sales.NewCurrency
EXECUTE Sales.uspInsertNewCurrency @CurrencyCode = 'CAD'

SELECT CurrencyCode, Name                                       -- Смотрим содержимое Sales.NewCurrency
FROM Sales.NewCurrency
