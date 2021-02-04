SELECT
USER_NAME() AS 'User',
SUSER_SNAME() AS 'Login',
HOST_NAME() AS 'Workstation',
APP_NAME() AS 'Application';