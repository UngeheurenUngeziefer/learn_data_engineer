USE AdventureWorks2019

GO
CREATE PROCEDURE Sales.uspGetCurrencyRate
@CurrencyRateIDList varchar(50)
AS
DECLARE @SQLString nvarchar(1000)
SET @SQLString = N'
SELECT CurrencyRateID, CurrencyRateDate, FromCurrencyCode,
ToCurrencyCode, AverageRate, EndOfDayRate
FROM Sales.CurrencyRate
WHERE CurrencyRateID in ('+@CurrencyRateIDList+');'
EXECUTE sp_executesql @SQLString;
GO
EXECUTE Sales.uspGetCurrencyRate @CurrencyRateIDList = '1, 4, 6, 7'

GO
DROP PROCEDURE Sales.uspGetCurrencyInformation

GO
CREATE PROCEDURE Sales.uspGetCurrencyInformation
@CurrencyCodeList varchar(200) = 'USD'
AS
DECLARE @SQLString nvarchar(1000)
SET @SQLString = N'
SELECT CurrencyCode, Name
FROM Sales.Currency
WHERE CurrencyCode in ('+@CurrencyCodeList+');'
EXECUTE sp_executesql @SQLString;
GO
EXECUTE Sales.uspGetCurrencyInformation
@CurrencyCodeList = '''USD'', ''AUD'', ''CAD'', ''MXN''';


GO
DROP PROCEDURE Sales.uspGetCurrencyInformation

GO
CREATE PROCEDURE Sales.uspGetCurrencyInformationXML
@XMLList varchar(1000)
AS
DECLARE @XMLDocHandle int
DECLARE @CurrencyCodeTable table
(
CurrencyCode char(3)
)
EXECUTE sp_xml_preparedocument @XMLDocHandle OUTPUT, @XMLList;
INSERT INTO @CurrencyCodeTable(CurrencyCode)
SELECT CurrencyCode
FROM OPENXML (@XMLDocHandle, '/ROOT/Currency',1)
WITH (
CurrencyCode char(3)
);
SELECT c.CurrencyCode, c.Name, c.ModifiedDate
FROM Sales.Currency c
JOIN @CurrencyCodeTable tvp
ON c.CurrencyCode = tvp.CurrencyCode;
EXECUTE sp_xml_removedocument @XMLDocHandle
GO
--Execute the stored procedure, passing in XML
EXECUTE Sales.uspGetCurrencyInformationXML @XMLList ='
<ROOT>
<Currency CurrencyCode="USD"> </Currency>
<Currency CurrencyCode="AUD"> </Currency>
<Currency CurrencyCode="CAD"> </Currency>
<Currency CurrencyCode="MXN"> </Currency>
</ROOT>'
