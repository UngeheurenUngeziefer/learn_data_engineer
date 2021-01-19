SELECT *
FROM sys.dm_os_wait_stats
ORDER BY waiting_tasks_count DESC

SELECT *
FROM sys.dm_db_index_usage_stats

-- to show statistic and execution time
-- SET STATISTICS TIME ON
-- SET STATISTICS IO ON

--SELECT name, collation_name  
--FROM sys.databases