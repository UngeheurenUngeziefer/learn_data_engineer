USE TESTSQL

CREATE TABLE h_region (
	R_REGIONKEY INT,
	R_NAME VARCHAR(50), 
	R_COMMENT VARCHAR(255)
)

SELECT * FROM h_region
DROP TABLE h_region

CREATE TABLE h_nation (
	nation_key INT,
	[name] VARCHAR(50),
	region_key INT,
	comment VARCHAR(255)
)

SELECT * FROM h_nation