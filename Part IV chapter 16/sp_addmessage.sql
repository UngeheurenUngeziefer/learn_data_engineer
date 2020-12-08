EXEC sp_addmessage 50001, 16, 'Unable to update %s';

EXEC sp_addmessage 50001, 16,
'Update error on %s', @replace = 'replace';

SELECT *
FROM sys.messages
WHERE message_id > 50000;

SELECT 'EXEC sp_addmessage, '
+ CAST(message_id AS VARCHAR(7))
+ ', ' + CAST(severity AS VARCHAR(2))
+ ', ''' + [text] + ''';'
FROM sys.messages
WHERE message_id > 50000;

EXEC sp_dropmessage 50001;