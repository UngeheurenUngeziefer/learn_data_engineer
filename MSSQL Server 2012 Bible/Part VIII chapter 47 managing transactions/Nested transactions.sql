SELECT @@TRANCOUNT; -- 0
BEGIN TRAN;
    SELECT @@TRANCOUNT; -- 1
    BEGIN TRAN;
        SELECT @@TRANCOUNT; -- 2
        BEGIN TRAN;
            SELECT @@TRANCOUNT; -- 3
            ROLLBACK; -- undoes all nested transactions
SELECT @@TRANCOUNT; -- 0