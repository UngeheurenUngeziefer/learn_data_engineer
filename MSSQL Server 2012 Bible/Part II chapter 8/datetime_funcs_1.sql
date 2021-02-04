SELECT GetDate() AS current_server_date,
       CURRENT_TIMESTAMP AS except_ANSI_standard,
       GetUTCDate() AS greenwich_mean_time,
       SYSDATETIME() AS to_the_nearest_hundred_nanoseconds,
       SysUTCDateTime() AS greenwich_nanosec,
       SYSDATETIMEOFFSET() AS date_time_offset
       
