IF NOT EXISTS(
    SELECT * FROM tempdb.sys.objects
    WHERE name = '##TempWork')
  
    CREATE TABLE ##TempWork(
        PK INT PRIMARY KEY,
        Col1 INT
    );