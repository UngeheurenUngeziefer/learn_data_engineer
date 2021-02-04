USE AdventureWorksLT2019
SELECT CST.CompanyName, SOH.TotalDue
FROM SalesLT.Customer CST
LEFT OUTER JOIN SalesLT.SalesOrderHeader SOH
ON CST.CustomerID = SOH.CustomerID
ORDER BY CST.CompanyName

USE tempdb
GO
CREATE TABLE dbo.Customer2 (
             CustomerID INT ,
             LastName VARCHAR(50));
CREATE TABLE dbo.SalesOrder2 (
             OrderNumber VARCHAR(15),
             CustomerID INT);

INSERT Customer2 (CustomerID,LastName)
VALUES(101, 'Smith'),
      (102, 'Adams'),
      (103, 'Reagan');
INSERT SalesOrder2 (OrderNumber ,CustomerID )
VALUES( '1',102),
      ( '2',104),
      ( '3',105);

-- only intersected
SELECT c.CustomerID, c.LastName, so.OrderNumber
FROM dbo.Customer2 c
INNER JOIN dbo.SalesOrder2 so
ON c.CustomerID = so.CustomerID

-- all left + intersected from right
SELECT c.CustomerID, c.LastName , so.OrderNumber
FROM dbo.Customer2 c
LEFT OUTER JOIN dbo.SalesOrder2 so
ON c.CustomerID = so.CustomerID

-- all right + intersected from left
SELECT c.CustomerID, c.LastName , so.OrderNumber
FROM dbo.Customer2 c
RIGHT OUTER JOIN dbo.SalesOrder2 so
ON c.CustomerID = so.CustomerID

-- all records
SELECT c.CustomerID, c.LastName , so.OrderNumber
FROM dbo.Customer2 c
FULL OUTER JOIN dbo.SalesOrder2 so
ON c.CustomerID = so.CustomerID

-- left join and where condition
SELECT c.CustomerID, c.LastName, so.OrderNumber
FROM dbo.Customer2 c
LEFT OUTER JOIN dbo.SalesOrder2 so
ON c.CustomerID = so.CustomerID
WHERE c.LastName = 'Adams'

