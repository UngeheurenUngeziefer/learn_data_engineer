CREATE PROCEDURE Sales.uspGetCurrencyRatesXML
    @XMLList varchar(1000), 
    @CurrencyRateDate datetime
AS
DECLARE @XMLDocHandle int
DECLARE @CurrencyCodeTable table
(
    FromCurrencyCode char(3),
    ToCurrencyCode char(3)
)
EXECUTE sp_xml_preparedocument @XMLDocHandle OUTPUT, @XMLlist
INSERT INTO @CurrencyCodeTable(FromCurrencyCode, ToCurrencyCode)
SELECT FromCurrencyCode, ToCurrencyCode
FROM OPENXML (@XMLDocHandle, '/ROOT/CurrencyList',1)
WITH (
    FromCurrencyCode char(3),
    ToCurrencyCode char(3)
    );
SELECT cr.CurrencyRateID, cr.FromCurrencyCode,
       cr.ToCurrencyCode, cr.AverageRate,
       cr.EndOfDayRate, cr.CurrencyRateDate
FROM Sales.CurrencyRate cr
JOIN @CurrencyCodeTable tvp
ON cr.FromCurrencyCode = tvp.FromCurrencyCode
AND cr.ToCurrencyCode = tvp.ToCurrencyCode
WHERE CurrencyRateDate = @CurrencyRateDate
EXECUTE sp_xml_removedocument @XMLDocHandle

GO
--Execute the stored procedure
EXECUTE Sales.uspGetCurrencyRatesXML @XMLList ='
<ROOT>
<CurrencyList FromCurrencyCode="USD" ToCurrencyCode="AUD"> </CurrencyList>
<CurrencyList FromCurrencyCode="USD" ToCurrencyCode="EUR"> </CurrencyList>
<CurrencyList FromCurrencyCode="USD" ToCurrencyCode="GBP"> </CurrencyList>
<CurrencyList FromCurrencyCode="USD" ToCurrencyCode="MXN"> </CurrencyList>
</ROOT>', @CurrencyRateDate = '2005-07-14'

GO
CREATE TYPE CurrencyCodeListType as TABLE
(
    FromCurrencyCode char(3),
    ToCurrencyCode char(3)
)

GO
CREATE PROCEDURE Sales.uspGetCurrencyRatesUDT
@CurrencyCodeTable as CurrencyCodeListType READONLY,
@CurrencyRateDate date
AS
SELECT cr.CurrencyRateID, cr.FromCurrencyCode,
       cr.ToCurrencyCode, cr.AverageRate,
       cr.EndOfDayRate, cr.CurrencyRateDate
FROM Sales.CurrencyRate cr
JOIN @CurrencyCodeTable tvp
ON cr.FromCurrencyCode = tvp.FromCurrencyCode
AND cr.ToCurrencyCode = tvp.ToCurrencyCode
WHERE CurrencyRateDate = @CurrencyRateDate

GO
DECLARE @CurrencyCodeTVP as CurrencyCodeListType
INSERT INTO @CurrencyCodeTVP(FromCurrencyCode, ToCurrencyCode)
VALUES
('USD', 'AUD'),
('USD', 'GBP'),
('USD', 'CAD'),
('USD', 'MXN');
EXECUTE Sales.uspGetCurrencyRatesUDT
@CurrencyCodeTable = @CurrencyCodeTVP,
@CurrencyRateDate = '2005-07-14'
