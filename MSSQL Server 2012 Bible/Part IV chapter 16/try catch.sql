BEGIN TRY
    SELECT 'Try One';
    RAISERROR('Simulated Error', 16, 1);
    SELECT 'Try Two';
END TRY
BEGIN CATCH
    SELECT 'Catch Block';
END CATCH;
SELECT 'Post Try';