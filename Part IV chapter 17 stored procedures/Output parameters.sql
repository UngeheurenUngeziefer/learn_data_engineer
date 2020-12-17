USE AdventureWorks2019

GO
CREATE PROCEDURE Sales.uspGetCurrencyName          -- создаём процедуру
    @CurrencyCode char(3),                         -- принимающую две переменные
    @CurrencyName varchar(50) OUTPUT               -- одна переменная с командой OUTPUT
AS
SELECT @CurrencyName = Name                        -- 
FROM Sales.Currency
WHERE CurrencyCode = @CurrencyCode;

GO
DECLARE @CurrencyNameOutput varchar(50);           -- объявляем переменную чтобы получить выходной параметр
EXECUTE Sales.uspGetCurrencyName                   -- исполняем хранимую процедуру
    @CurrencyCode = 'USD',                         -- где код USD
    @CurrencyName = @CurrencyNameOutput OUTPUT     -- выводится имя
PRINT @CurrencyNameOutput                          -- напечатаем его 
