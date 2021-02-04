USE AdventureWorks2019
ALTER DATABASE AdventureWorks2012
SET ALLOW_SNAPSHOT_ISOLATION ON
-- check snapshot isolation
select name,
snapshot_isolation_state,
snapshot_isolation_state_desc,
is_read_committed_snapshot_on
from sys.databases
where database_id = DB_ID()


USE AdventureWorks2019
SET TRANSACTION ISOLATION LEVEL SNAPSHOT
BEGIN TRAN
SELECT LastName
FROM Person.Person
WHERE BusinessEntityID = 1

USE AdventureWorks2019;
SET TRANSACTION ISOLATION LEVEL SNAPSHOT
BEGIN TRAN
UPDATE Person.Person
SET LastName = 'Chapman'
WHERE BusinessEntityID = 1
SELECT LastName
FROM Person.Person
WHERE BusinessEntityID = 1

SELECT LastName
FROM Person.Person
WHERE BusinessEntityID = 1