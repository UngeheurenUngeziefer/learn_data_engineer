SELECT *
FROM sys.dm_os_wait_stats
ORDER BY waiting_tasks_count DESC

SELECT *
FROM sys.dm_db_index_usage_stats

-- to show statistic and execution time
-- SET STATISTICS TIME ON
-- SET STATISTICS IO ON

-- SELECT name, collation_name  
-- FROM sys.databases

-- DBCC FREEPROCCACHE

SELECT cacheobjtype, objtype, usecounts, refcounts,
		[text] as SQLText, query_plan
FROM sys.dm_exec_cached_plans
CROSS APPLY sys.dm_exec_sql_text(plan_handle)
CROSS APPLY sys.dm_exec_query_plan(plan_handle)

