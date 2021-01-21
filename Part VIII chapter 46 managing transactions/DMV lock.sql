SELECT session_id, blocking_session_id
FROM sys.dm_exec_requests
WHERE blocking_session_id > 0

-- Viewing all the locks is possible with the sys.dm_tran_locks DMV
SELECT
request_session_id as Spid,
Coalesce(s.name + '.' + o.name + isnull('.' + i.name,''),
s2.name + '.' + o2.name COLLATE SQL_Latin1_General_CP1_CI_AS,
db.name) AS Object,
l.resource_type as Type,
request_mode as Mode,
request_status as Status
FROM sys.dm_tran_locks l
LEFT JOIN sys.partitions p
ON l.resource_associated_entity_id = p.hobt_id
LEFT JOIN sys.indexes i
ON p.object_id = i.object_id
AND p.index_id = i.index_id
LEFT JOIN sys.objects o
ON p.object_id = o.object_id
LEFT JOIN sys.schemas s
ON o.schema_id = s.schema_id
LEFT JOIN sys.objects o2
ON l.resource_associated_entity_id = o2.object_id
LEFT JOIN sys.schemas s2
ON o2.schema_id = s2.schema_id
LEFT JOIN sys.databases db
ON l.resource_database_id = db.database_id
WHERE resource_database_id = DB_ID()
ORDER BY Spid, Object, CASE l.resource_type
When 'database' Then 1
when 'object' then 2
when 'page' then 3
when 'key' then 4
Else 5 end