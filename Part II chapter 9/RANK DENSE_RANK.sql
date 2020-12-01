USE AdventureWorks2019

GO
SELECT ProductID, COUNT(*) as [Count]
FROM Sales.SalesOrderDetail
GROUP BY ProductID
ORDER BY COUNT(*)

GO
SELECT ProductID, SalesCount, RANK() OVER(ORDER BY SalesCount) as [Rank],
       DENSE_RANK() OVER(Order By SalesCount) as [DenseRank]
FROM (SELECT ProductID, COUNT(*) as SalesCount
    FROM Sales.SalesOrderDetail
    GROUP BY ProductID) AS Q
ORDER BY [Rank]

