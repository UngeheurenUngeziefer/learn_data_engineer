DECLARE @Test INT,
        @TestTwo NVARCHAR(25);
SELECT @Test, @TestTwo;
SET @Test = 1;
SET @TestTwo = 'a value';
SELECT @Test, @TestTwo;
-- GO
-- SELECT @Test AS BatchTwo, @TestTwo;