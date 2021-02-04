USE AdventureWorks2019

SELECT sp.FirstName, sp.LastName, YEAR(soh.OrderDate) OrderYear, soh.TotalDue,
       SUM(soh.TotalDue) OVER
            (ORDER BY sp.FirstName ROWS UNBOUNDED PRECEDING) CumulativeTotal
FROM Sales.SalesOrderHeader soh
INNER JOIN Sales.vSalesPerson sp
ON soh.SalesPersonID = sp.BusinessEntityID
WHERE soh.SalesPersonID IN (274) OR
      (soh.OrderDate BETWEEN '1/1/2005' AND '12/31/2005')


SELECT sp.FirstName, sp.LastName, YEAR(soh.OrderDate) OrderYear, soh.TotalDue, 
    SUM(soh.TotalDue) OVER
    (ORDER BY sp.FirstName ROWS BETWEEN CURRENT ROW AND UNBOUNDED
    FOLLOWING) CumulativeTotal
FROM Sales.SalesOrderHeader soh
INNER JOIN Sales.vSalesPerson sp
ON soh.SalesPersonID = sp.BusinessEntityID
WHERE soh.SalesPersonID IN (274) OR
soh.OrderDate BETWEEN '1/1/2005' AND '12/31/2005'