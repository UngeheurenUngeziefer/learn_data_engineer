SET showplan_all ON
GO
SET showplan_all OFF
GO
SET Showplan_text ON
GO
SET Showplan_text OFF
GO
SET Showplan_xml ON
GO
SET Showplan_xml OFF
GO

USE TestSQL
SELECT TOP 100 productid, productname
FROM Production.Products prod
LEFT JOIN Production.Categories cat
ON cat.categoryid = prod.categoryid
ORDER BY cat.categoryid

