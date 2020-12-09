SELECT message_id, severity, language_id, text
FROM master.sys.messages
WHERE language_id = 1033 -- US English
AND severity >= 19
ORDER BY severity, message_id;