Use AdventureWorks2019
go
CREATE TABLE dbo.Test (
[Name] NVARCHAR(50)
);
go
CREATE VIEW dbo.vTest
WITH SCHEMABINDING
AS
SELECT [Name] FROM dbo.Test;
go
use AdventureWorks2019
go
ALTER TABLE Test
ALTER COLUMN [Name] NVARCHAR(100);