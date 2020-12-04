USE AdventureWorks2019

-- create a table
GO
CREATE TABLE dbo.[Address]
(
AddressID int identity(1,1)
CONSTRAINT PK_Address_AddressID PRIMARY KEY,
	Address1 varchar(75) NOT NULL,
	City varchar(75) NOT NULL,
	State char(3) NOT NULL,
	County varchar(50) NULL,
	PostalCode varchar(10)
)

-- insert some values
GO
INSERT INTO dbo.Address(City, State, Address1, PostalCode)
VALUES('Houston', 'TX', '1411 Mesa Road', 77016);
INSERT INTO dbo.Address(City, State, Address1, County, PostalCode)
VALUES('Baton Rouge', 'LA', '444 Perkins Road', 'East Baton Rouge',
70808), ('Chicago', 'IL', '8765 Buttonwood Walk', 'Cook', 60429);

-- inserting more values
INSERT INTO dbo.Address
VALUES('3333 Pike Street', 'Seattle', 'WA','Pike', '23674');

-- add a row with determined id
SET IDENTITY_INSERT dbo.Address ON
INSERT INTO dbo.Address(AddressID, Address1, City, State, County,
PostalCode)
VALUES(999, '444 Our Way', 'Detroit', 'MI','Pike', '66666');
SET IDENTITY_INSERT dbo.Address OFF

-- insert value as expression
INSERT INTO dbo.Address
VALUES('99934' + ' Orange Ct', 'Memphis', 'TN','Vols', '74944');

-- show the table
SELECT AddressID, City, State, Address1, County, PostalCode
FROM dbo.Address;