USE DWH

-- FIRST DIMENSION ------------------------------------------|
-- creating new table for denormalized h_region and h_nation
CREATE TABLE h_region_h_nation (
	R_REGIONKEY INT,
	R_NAME VARCHAR(25),
	R_COMMENT VARCHAR(250),
	N_NATIONKEY INT PRIMARY KEY,
	N_NAME VARCHAR(25),
	N_COMMENT VARCHAR(250)
)

-- inserting two tables into one
INSERT INTO h_region_h_nation
SELECT *
FROM h_region reg
LEFT JOIN h_nation nat
ON reg.R_REGIONKEY = nat.N_REGIONKEY

-- checking insertion
SELECT * FROM h_region_h_nation
ORDER BY N_NATIONKEY


-- creating one dimension for star schema from three tables
CREATE TABLE h_supplier_h_region_h_nation (
	S_SUPPKEY INT PRIMARY KEY,
	S_NAME VARCHAR(50),
	S_ADDRESS VARCHAR(250),
	S_PHONE VARCHAR(50),
	S_ACCTBAL VARCHAR(20),
	S_COMMENT VARCHAR(250),
	R_REGIONKEY INT,
	R_NAME VARCHAR(25),
	R_COMMENT VARCHAR(250),
	N_NATIONKEY INT,
	N_NAME VARCHAR(25),
	N_COMMENT VARCHAR(250)
)

-- inserting three tables into one
INSERT INTO h_supplier_h_region_h_nation
SELECT [S_SUPPKEY],[S_NAME],[S_ADDRESS],[S_PHONE],[S_ACCTBAL],[S_COMMENT],[R_REGIONKEY],
	   [R_NAME],[R_COMMENT],[N_NATIONKEY],[N_NAME],[N_COMMENT]
FROM h_supplier sup
LEFT JOIN h_region_h_nation regnat
ON sup.S_NATIONKEY = regnat.N_NATIONKEY

-- checking insertion
SELECT * FROM h_supplier_h_region_h_nation


-- SECOND DIMENSION ------------------------------------------|
-- creating second dimension for star schema from two tables
CREATE TABLE h_order_h_customer (
	O_ORDERKEY INT,
	O_CUSTKEY INT,
	O_ORDERSTATUS VARCHAR(1),
	O_TOTALPRICE VARCHAR(25),
	O_ORDERDATE VARCHAR(8),
	O_ORDERPRIORITY VARCHAR(25),
	O_CLERK VARCHAR(20),
	O_SHIPPRIORITY INT,
	O_COMMENT VARCHAR(250),
	C_NAME VARCHAR(25),
	C_ADDRESS VARCHAR(250),
	C_NATIONKEY INT,
	C_PHONE VARCHAR(12),
	C_ACCTBAL VARCHAR(20),
	C_MKTSEGMENT VARCHAR(25),
	C_COMMENT VARCHAR(250)
)

INSERT INTO h_order_h_customer
SELECT O_ORDERKEY, O_CUSTKEY, O_ORDERSTATUS, O_TOTALPRICE,
	   O_ORDERDATE, O_ORDERPRIORITY, O_CLERK, O_SHIPPRIORITY,
	   O_COMMENT, C_NAME, C_ADDRESS, C_NATIONKEY, C_PHONE,
	   C_ACCTBAL, C_MKTSEGMENT,	C_COMMENT 
FROM h_order
LEFT JOIN h_customer
ON O_CUSTKEY = C_CUSTKEY

-- check insertion
SELECT * FROM  h_order_h_customer


-- THIRD DIMENSION IS h_part table alone----------------------|

--h_partsupp dont have unique PK's so we add it to fact table-|
CREATE TABLE h_lineitem_facttable (
	L_ORDERKEY INT,
	L_PARTKEY INT,
	L_SUPPKEY INT,
    L_LINENUMBER INT,
	L_QUANTITY INT,
	L_EXTENDEDPRICE VARCHAR(25),
	L_DISCOUNT VARCHAR(25),
	L_TAX VARCHAR(5),
	L_RETURNFLAG VARCHAR(1),
	L_LINESTATUS VARCHAR(1),
	L_SHIPDATE VARCHAR(8),
	L_COMMITDATE VARCHAR(8),
	L_RECEIPTDATE VARCHAR(8),
	L_SHIPINSTRUCT VARCHAR(30),
	L_SHIPMODE VARCHAR(20),
	L_COMMENT VARCHAR(250),
	PS_AVAILQTY INT,
	PS_SUPPLYCOST VARCHAR(10),
	PS_COMMENT VARCHAR(250),
)

SELECT * FROM h_lineitem_facttable


INSERT h_lineitem_facttable
SELECT [L_ORDERKEY],[L_PARTKEY],[L_SUPPKEY],
	   [L_LINENUMBER],[L_QUANTITY],[L_EXTENDEDPRICE],
	   [L_DISCOUNT],[L_TAX],[L_RETURNFLAG],[L_LINESTATUS],
	   [L_SHIPDATE],[L_COMMITDATE],[L_RECEIPTDATE],[L_SHIPINSTRUCT],
	   [L_SHIPMODE],[L_COMMENT], PS_AVAILQTY, PS_SUPPLYCOST, PS_COMMENT
FROM h_lineitem
LEFT JOIN h_partsupp
ON PS_PARTKEY = L_PARTKEY
AND PS_SUPPKEY = L_SUPPKEY

SELECT TOP 1000 * FROM h_partsupp



