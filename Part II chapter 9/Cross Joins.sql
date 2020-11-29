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

SELECT Customer2.CustomerID, Customer2.LastName, SalesOrder2.OrderNumber
FROM Customer2 
CROSS JOIN SalesOrder2