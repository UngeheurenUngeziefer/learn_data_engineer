DROP PROCEDURE IF EXISTS usp_cast_to_date
GO

-- cast varchar to date
CREATE PROCEDURE usp_cast_to_date
	@table_name NVARCHAR(30),
	@column NVARCHAR(30)
AS
BEGIN
	DECLARE @sql VARCHAR(700);
	SET @sql='
		SELECT ' + @column + '
		FROM ' + @table_name + '
		WHERE TRY_CONVERT(DATE, ' + @column + ') IS NULL'
	PRINT(@sql)
	EXECUTE(@sql)


END
GO

EXECUTE usp_cast_to_date @table_name = 'DWH.dbo.h_order_h_customer', @column = 'O_ORDERDATE'


