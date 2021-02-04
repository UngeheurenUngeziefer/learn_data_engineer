CREATE FUNCTION dbo.ufnCalculateQuotient        -- создаём функцию
(
    @Numerator numeric(5, 2),                   -- число 5 чисел до запятой, 2 после
    @Denominator numeric(5, 2) = 1.0            -- у делителя есть значение по умолчанию
)
RETURNS numeric(5,2)                            -- функция будет возвращать число
AS
BEGIN
    RETURN @Numerator/@Denominator;             -- функция будет делить числа
END

GO
SELECT dbo.ufnCalculateQuotient(12.1, 7.45),    -- делим числа передаваемые функции
       dbo.ufnCalculateQuotient (7.0, DEFAULT)  -- делим 7 на значение по умолчанию

USE AdventureWorks2019
GO
CREATE FUNCTION dbo.ufnGetOrderTotalByProduct(@ProductID int)           -- создаём функцию
RETURNS int                                                             -- возвращающую число
AS
BEGIN
    DECLARE @OrderTotal int;
    SELECT @OrderTotal = sum(sod.OrderQty)
    FROM Production.Product p
    JOIN Sales.SalesOrderDetail sod
    ON p.ProductID = sod.ProductID
    WHERE p.ProductID = @ProductID
    GROUP BY p.ProductID;
    RETURN @OrderTotal;                                                 -- общее число заказов
END

GO
SELECT p.Name, dbo.ufnGetOrderTotalByProduct(p.ProductID) as OrderTotal -- результатом получим
FROM Production.Product p                                               -- общее число заказов
ORDER BY OrderTotal DESC;                                               -- для каждой компании
