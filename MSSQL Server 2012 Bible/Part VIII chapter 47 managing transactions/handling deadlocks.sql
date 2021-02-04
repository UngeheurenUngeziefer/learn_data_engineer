USE AdventureWorks2019

DECLARE @retry INT
SET @retry = 1
WHILE @retry = 1
    BEGIN
        BEGIN TRY
        SET @retry = 0
            BEGIN TRANSACTION
            UPDATE HumanResources.Department
            SET Name = 'Accounting'
            WHERE DepartmentID = 2;
            UPDATE HumanResources.Department
            SET Name = 'Development'
            WHERE DepartmentID = 1;
            
            COMMIT TRANSACTION
        END TRY
        BEGIN CATCH
            IF ERROR_NUMBER() = 1205
            BEGIN
                PRINT ERROR_MESSAGE()
                SET @retry = 1
            END
        ROLLBACK TRANSACTION
        END CATCH
    END

    SET DEADLOCK_PRIORITY LOW