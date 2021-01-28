SET TRANSACTION ISOLATION LEVEL
READ COMMITTED;

SELECT TIL.Description
FROM sys.dm_exec_sessions dmv
JOIN (VALUES(1, 'Read Uncommitted'),
(2, 'Read Committed'),
(3, 'Repeatable Read'),
(4, 'Serializable'))
AS TIL(ID, Description)
ON dmv.transaction_isolation_level = TIL.ID
WHERE session_id = @@spid;

SET TRANSACTION ISOLATION LEVEL
REPEATABLE READ;
SELECT Name
FROM HumanResources.Department WITH (NOLOCK)
WHERE DepartmentID = 1;