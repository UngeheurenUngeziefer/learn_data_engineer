SELECT *
FROM sys.dm_exec_describe_first_result_set_for_object
(OBJECT_ID(N'dbo.uspGetEmployeeManagers'), 0)