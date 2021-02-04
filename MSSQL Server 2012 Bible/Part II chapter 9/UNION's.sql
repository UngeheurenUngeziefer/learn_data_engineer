-- temporary table
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

-- UNION ALL
SELECT CustomerID, 'Customer2 - Source' as Source
FROM dbo.Customer2
UNION ALL
SELECT CustomerID, 'SalesOrder2 - Source'
FROM dbo.SalesOrder2
ORDER BY 1;

-- INTERSECT
SELECT CustomerID
FROM dbo.Customer2
INTERSECT
SELECT CustomerID
FROM dbo.SalesOrder2
ORDER BY 1;

-- EXCEPT
SELECT CustomerID
FROM dbo.Customer2
EXCEPT
SELECT CustomerID
FROM dbo.SalesOrder2
ORDER BY 1;