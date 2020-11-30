-- multiple condition joins
FROM A
INNER JOIN B
    ON A.col = B.col
INNER JOIN C
    ON B.col = C.col
    AND A.col = C.col;

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

-- LEFT SET DIFFERENCE QUERY
USE tempdb
SELECT c.CustomerID, c.LastName, so.OrderNumber
FROM dbo.Customer2 c
LEFT OUTER JOIN dbo.SalesOrder2 so 
ON c.CustomerID = so.CustomerID 
WHERE so.OrderNumber IS NULL

-- FULL SET DIFFERENCE QUERIES
SELECT c2.CustomerID c2CustomerID, so2.CustomerID so2CustomerID
FROM dbo.Customer2 c2
FULL OUTER JOIN dbo.SalesOrder2 so2
ON c2.CustomerID = so2.CustomerID
WHERE c2.CustomerID IS NULL
OR so2.CustomerID IS NULL;

