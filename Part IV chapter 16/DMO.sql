USE AdventureWorks2019
GO
SELECT s.NAME + '.' + o2.NAME AS 'Table', pk.NAME AS 'Primary Key'
FROM sys.key_constraints AS pk
JOIN sys.objects AS o
ON pk.OBJECT_ID = o.OBJECT_ID
JOIN sys.objects AS o2
ON o.parent_object_id = o2.OBJECT_ID
JOIN sys.schemas AS s
ON o2.schema_id = s.schema_id;

USE AdventureWorks2019
GO
sp_help 'Production.Product';