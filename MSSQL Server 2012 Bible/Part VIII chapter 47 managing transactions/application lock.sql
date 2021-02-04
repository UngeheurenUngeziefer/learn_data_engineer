BEGIN TRANSACTION
DECLARE @ShareOK INT
EXEC @ShareOK = sp_GetAppLock
@Resource = 'TimChapman',
@LockMode = 'Exclusive'
IF @ShareOK < 0
--Error handling code
--code

EXEC sp_ReleaseAppLock @Resource = 'TimChapman'
COMMIT TRANSACTION

EXECUTE sp_Lock