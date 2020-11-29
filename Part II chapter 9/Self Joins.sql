-- sample data
USE tempdb
CREATE TABLE dbo.Employee (
    EmployeeID int PRIMARY KEY,
    EmployeeName varchar(30),
    MgrID int FOREIGN KEY REFERENCES Employee(EmployeeID))
INSERT INTO dbo.Employee
VALUES  (1, 'Janet Jones', NULL),
        (2, 'Tom Smith', 1),
        (3, 'Ted Adams', 2),
        (4, 'Mary Thomas', 2),
        (5, 'Jack Jones', 2),
        (6, 'Anita Kidder', 3),
        (7, 'William Owens', 3),
        (8, 'Sean Watson', 4),
        (9, 'Brenda Jackson', 5),
        (10, 'Frank Johnson', 5)

-- self join, connect different data from same table
SELECT Mgr.EmployeeName MgrName, Mgr.EmployeeID EmpIDMgr, Emp.EmployeeName, Emp.EmployeeID
FROM dbo.Employee Emp 
JOIN dbo.Employee Mgr
ON Emp.MgrID = Mgr.EmployeeID
