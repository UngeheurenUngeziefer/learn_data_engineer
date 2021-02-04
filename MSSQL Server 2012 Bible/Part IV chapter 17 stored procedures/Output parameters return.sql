USE AdventureWorks2019

GO
ALTER PROCEDURE Sales.uspGetCurrencyName                -- изменяем процедуру
    @CurrencyCode char(3),
    @CurrencyName varchar(50) OUTPUT
AS
SELECT @CurrencyName = Name
FROM Sales.Currency
WHERE CurrencyCode = @CurrencyCode;
IF @CurrencyName IS NULL                                -- если имя валюты неизвестно
BEGIN
    RETURN 1                                            -- вернём 1
END
ELSE
BEGIN
    RETURN 0                                            -- иначе вернём 0
END;

GO
DECLARE @CurrencyNameOutput varchar(50)
DECLARE @ReturnCode int;
EXECUTE @ReturnCode = Sales.uspGetCurrencyName          -- исполним процедуру
        @CurrencyCode = 'USD',                          -- передадим код USD
        @CurrencyName = @CurrencyNameOutput OUTPUT      -- вывод
PRINT @CurrencyNameOutput                               -- напечатаем вывод
PRINT @ReturnCode                                       -- возвращается 0 так как имя 
                                                        -- валюты известно (не NULL)
