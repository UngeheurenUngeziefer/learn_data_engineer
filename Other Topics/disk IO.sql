USE MASTER
GO
 
DECLARE @DML nvarchar(MAX)
 
DECLARE @SQLShackIOStatistics TABLE
(
[I/ORank] [int] NULL,
[DBName] [nvarchar](128) NULL,
[driveLetter] [nvarchar](1) NULL,
[totalNumOfWrites] [bigint] NULL,
[totalNumOfBytesWritten] [bigint] NULL,
[totalNumOfReads] [bigint] NULL,
totalNumOfBytesRead [bigint] NULL,
[totalI/O(MB)] [decimal](12,2) NULL,
[I/O(%)] [decimal](5, 2) NULL,
[SizeOfFile] [decimal](10,2) NULL
)
SET @DML='
WITH SQLShackIOStatistics
AS
(
select 
db_name(mf.database_id) as dbname, 
left(mf.physical_name, 1) as driveLetter, 
sum(vfs.num_of_writes) [totalNumOfWrites],
sum(vfs.num_of_bytes_written) [totalNumOfBytesWritten],
sum(vfs.num_of_reads) [totalNumOfReads], 
sum(vfs.num_of_bytes_read) [totalNumOfBytesRead], 
cast(SUM(num_of_bytes_read + num_of_bytes_written)/1024 AS DECIMAL(12, 2)) AS [TotIO(MB)],
MAX(cast(vfs.size_on_disk_bytes/1024/1024.00 as decimal(10,2))) SizeMB
from sys.master_files mf
join sys.dm_io_virtual_file_stats(NULL, NULL) vfs
on mf.database_id=vfs.database_id and mf.file_id=vfs.file_id
GROUP BY mf.database_id,left(mf.physical_name, 1))
SELECT 
	ROW_NUMBER() OVER(ORDER BY [TotIO(MB)] DESC) AS [I/ORank],
	[dbname],
	driveLetter,
	[totalNumOfWrites],
	totalNumOfBytesWritten,
	totalNumOfReads,
	totalNumOfBytesRead,
	[TotIO(MB)] AS [I/O(MB)],
	CAST([TotIO(MB)]/ SUM([TotIO(MB)]) OVER() * 100.0 AS DECIMAL(5,2)) AS [I/O(%)],
	SizeMB
	FROM SQLShackIOStatistics
	ORDER BY [I/ORank]
OPTION (RECOMPILE)
'
INSERT INTO @SQLShackIOStatistics
EXEC sp_executesql @DML
 
--SELECT * FROM @SQLShackIOStatistics
 
 
select [DBName],
[I/O Rank] = 
   STUFF(
(SELECT ',' + cast(s.[I/ORank] as varchar(3))
FROM @SQLShackIOStatistics s
WHERE s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,''),
physicalName=STUFF(
(SELECT ',' + s.driveLetter
FROM @SQLShackIOStatistics s
WHERE  s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,'') ,
FileSizeMB=STUFF(
(SELECT ',' + cast(s.SizeOfFile as varchar(20))
FROM @SQLShackIOStatistics s
WHERE  s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,'') ,
total_num_of_writes=STUFF(
(SELECT ',' + cast(s.[totalNumOfWrites] as varchar(20))
FROM @SQLShackIOStatistics s
WHERE  s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,''),
total_num_of_bytes_written=STUFF(
(SELECT ',' + cast(s.[totalNumOfBytesWritten] as varchar(20))
FROM @SQLShackIOStatistics s
WHERE  s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,''),
total_num_of_reads=STUFF(
(SELECT ',' + cast(s.totalnumofreads as varchar(20))
FROM @SQLShackIOStatistics s
WHERE  s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,''),
total_num_of_Bytes_reads=STUFF(
(SELECT ',' + cast(s.totalNumOfBytesRead as varchar(20))
FROM @SQLShackIOStatistics s
WHERE  s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,''),
[Total I/O (MB)]=STUFF(
(SELECT ',' + cast(s.[TotalI/O(MB)] as varchar(20))
FROM @SQLShackIOStatistics s
WHERE  s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,''),
[I/O Percent]=STUFF(
(SELECT ',' + cast(s.[I/O(%)] as varchar(20))
FROM @SQLShackIOStatistics s
WHERE  s.[DBName] = t.[DBName]
FOR XML PATH('')),1,1,'')
from @SQLShackIOStatistics t
group by [DBName]