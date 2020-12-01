USE AdventureWorks2019

GO
WITH YearlyCountryRegionSales AS
(SELECT [Group] AS CtryReg, Year(soh.OrderDate) OrYr, SUM(TotalDue) TotalDueYTD
FROM Sales.SalesOrderHeader soh
INNER JOIN Sales.SalesTerritory st
ON soh.TerritoryID = st.TerritoryID
GROUP BY
[Group], Year(soh.OrderDate))

SELECT CtryReg, OrYr, TotalDueYTD CurrentYearTotals, SUM(TotalDueYTD)
OVER(PARTITION BY CtryReg ORDER BY OrYr ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) - TotalDueYTD
PreviousYearTotals, SUM(TotalDueYTD)
OVER(PARTITION BY CtryReg ORDER BY OrYr
ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) - TotalDueYTD
NextYearTotals
FROM YearlyCountryRegionSales

