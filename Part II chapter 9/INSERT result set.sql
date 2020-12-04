USE AdventureWorks2019

GO
INSERT INTO Address
SELECT TOP(10)
AddressLine1, City, sp.StateProvinceCode, 'Sunshine', PostalCode
FROM Person.Address a
INNER JOIN Person.StateProvince sp
ON a.StateProvinceID = sp.StateProvinceID
WHERE sp.Name = 'California'

SELECT AddressID, City, State, Address1, County, PostalCode
FROM dbo.Address