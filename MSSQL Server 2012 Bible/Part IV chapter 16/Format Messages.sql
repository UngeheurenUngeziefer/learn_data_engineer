USE AdventureWorks2019;
GO
IF NOT EXISTS (SELECT * FROM sys.messages WHERE message_id = 50003)
BEGIN
EXECUTE sp_addmessage 50003, 16, 'Custom message for sys.messages';
END
GO
DECLARE @Message nvarchar(2000);
SELECT @Message = FORMATMESSAGE(50003);
BEGIN TRY
INSERT INTO Person.BusinessEntity
(BusinessEntityID, rowguid, ModifiedDate)
VALUES(1, newid(), getdate());
END TRY
BEGIN CATCH
THROW 50003, @Message, 1;
END CATCH;