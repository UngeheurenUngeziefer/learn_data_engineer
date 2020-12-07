USE AdventureWorks2019
DECLARE @MAV varchar(max)
SELECT @MAV = Coalesce(@MAV + ', '+ d.Name, d.Name)
FROM (
    SELECT Name
    FROM HumanResources.Department
) d
ORDER BY d.Name;
SELECT @MAV;

SELECT [text()] = Name + ','
FROM (
    SELECT DISTINCT Name
    FROM HumanResources.Department) d
ORDER BY Name
FOR XML PATH('');
