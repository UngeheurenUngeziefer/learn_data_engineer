DECLARE @Temp INT;
SET @Temp = 0;
WHILE @Temp < 3
BEGIN;
PRINT 'tested condition' + STR(@Temp);
SET @Temp = @Temp + 1;
END;
