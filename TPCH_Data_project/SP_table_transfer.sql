USE StagingDB
GO

DROP PROCEDURE IF EXISTS usp_TableTransfer
GO

-- sp that transfer data from StagingDB to DWH
CREATE PROCEDURE usp_TableTransfer 
	@table_name NVARCHAR(30),
	@columns NVARCHAR(250)
AS
BEGIN
	DECLARE @sql VARCHAR(700);
	SET @sql='
		INSERT INTO [DWH].[dbo].' + @table_name + '(' + @columns + ')
		SELECT ' + @columns + '
		FROM [StagingDB].[dbo].' + @table_name
	PRINT(@sql)
	EXECUTE(@sql)

END
GO


-- executing h_region
EXECUTE usp_TableTransfer @table_name = 'h_region', @columns = 'R_REGIONKEY, R_NAME, R_COMMENT'
GO

-- executing h_nation
EXECUTE usp_TableTransfer @table_name = 'h_nation', @columns = '[N_NATIONKEY], [N_NAME],[N_REGIONKEY],[N_COMMENT]'
GO

-- executing h_supplier
EXECUTE usp_TableTransfer @table_name = 'h_supplier', @columns = '[S_SUPPKEY],[S_NAME],[S_ADDRESS],[S_NATIONKEY],\
[S_PHONE],[S_ACCTBAL],[S_COMMENT]'
GO

-- executing h_customer
EXECUTE usp_TableTransfer @table_name = 'h_customer', @columns = 'C_CUSTKEY,C_NAME,C_ADDRESS,C_NATIONKEY,C_PHONE,\
C_ACCTBAL,C_MKTSEGMENT,C_COMMENT'
GO

-- executing h_part
EXECUTE usp_TableTransfer @table_name = 'h_part', @columns = 'P_PARTKEY,P_NAME,P_MFGR,P_BRAND,P_TYPE,P_SIZE,\
P_CONTAINER,P_RETAILPRICE,P_COMMENT'
GO

-- executing h_partsupp
EXECUTE usp_TableTransfer @table_name = 'h_partsupp', @columns = '[PS_PARTKEY],[PS_SUPPKEY],[PS_AVAILQTY],\
[PS_SUPPLYCOST],[PS_COMMENT]'
GO

-- executing h_order
EXECUTE usp_TableTransfer @table_name = 'h_order', @columns = 'O_ORDERKEY,O_CUSTKEY,O_ORDERSTATUS,O_TOTALPRICE,\
O_ORDERDATE,O_ORDERPRIORITY,O_CLERK,O_SHIPPRIORITY,O_COMMENT'
GO

-- executing h_lineitem
EXECUTE usp_TableTransfer @table_name = 'h_lineitem', @columns = '[L_ORDERKEY],[L_PARTKEY],[L_SUPPKEY],[L_LINENUMBER],\
[L_QUANTITY],[L_EXTENDEDPRICE],[L_DISCOUNT],[L_TAX],[L_RETURNFLAG],[L_LINESTATUS],[L_SHIPDATE],[L_COMMITDATE],\
[L_RECEIPTDATE],[L_SHIPINSTRUCT],[L_SHIPMODE],[L_COMMENT]'
GO


-- check datatypes of StagingDB and DWH columns
sp_describe_first_result_set @tsql = N'SELECT * FROM [StagingDB].[dbo].[h_lineitem]'
GO
sp_describe_first_result_set @tsql = N'SELECT * FROM [DWH].[dbo].[h_lineitem]'
GO
