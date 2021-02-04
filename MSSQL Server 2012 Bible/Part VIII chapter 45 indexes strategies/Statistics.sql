USE AdventureWorks2019
DBCC SHOW_STATISTICS ('Person.Person',		-- the last time statistics were updated
IX_Person_LastName_FirstName_MiddleName);

DBCC FREEPROCCACHE;							-- clear the buffers
DBCC DROPCLEANBUFFERS;