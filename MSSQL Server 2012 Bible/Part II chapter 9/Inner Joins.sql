USE AdventureWorksLT2019

SELECT CST.CompanyName, SOH.TotalDue
FROM SalesLT.Customer CST
INNER JOIN SalesLT.SalesOrderHeader SOH
ON CST.CustomerID = SOH.CustomerID


USE tempdb;
CREATE TABLE [dbo].[Customer](
    [CustomerID] [int] NOT NULL,
    [LastName] [varchar](50) NOT NULL);
INSERT INTO Customer(CustomerID, LastName)
VALUES(101, 'Smith'),
    (102, 'Adams'),
    (103, 'Reagan'),
    (104, 'Franklin'),
    (105, 'Dowdry')
CREATE TABLE [dbo].[SalesOrder](
    [OrderNumber] [varchar](50) NOT NULL,
    [CustomerID] [int] NOT NULL);
INSERT INTO SalesOrder (OrderNumber, CustomerID)
VALUES('1',101), ('2',101), ('3',102), ('4',102), ('5',103), ('6',105), ('7',105)


USE tempdb;
SELECT CustomerID, LastName 
FROM Customer


SELECT cst.CustomerID, OrderNumber
FROM SalesOrder so
INNER JOIN Customer cst
ON so.CustomerID = cst.CustomerID;


USE AdventureWorksLT2019;
SELECT cst.CompanyName, prod.Name ProductName
FROM SalesLT.Customer cst
INNER JOIN SalesLT.SalesOrderHeader soh
ON cst.CustomerID = soh.CustomerID
INNER JOIN SalesLT.SalesOrderDetail sod
ON soh.SalesOrderID = sod.SalesOrderID
INNER JOIN SalesLT.Product prod
ON sod.ProductID = prod.ProductID
INNER JOIN SalesLT.ProductCategory pc
ON prod.ProductCategoryID = pc.ProductCategoryID
WHERE pc.Name = 'Cranksets'
ORDER BY cst.CompanyName, prod.Name;