/* automaticly generated alter query
   for view from context menu
*/
USE [AdventureWorks2019]
GO

/****** Object:  View [dbo].[vEmployeeList]    Script Date: 12/2/2020 5:05:49 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- creating a view
ALTER VIEW [dbo].[vEmployeeList]
AS
SELECT P.BusinessEntityID, P.Title, P.LastName,
	   P.FirstName, E.JobTitle
FROM Person.Person P
INNER JOIN HumanResources.Employee E
ON P.BusinessEntityID = E.BusinessEntityID
GO

-- drop query
USE [AdventureWorks2019]
GO

/****** Object:  View [dbo].[vEmployeeList]    Script Date: 12/2/2020 5:08:48 PM ******/
DROP VIEW [dbo].[vEmployeeList]
GO




