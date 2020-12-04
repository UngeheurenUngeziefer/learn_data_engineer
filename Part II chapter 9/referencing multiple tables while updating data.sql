USE AdventureWorks2019

CREATE TABLE dbo.Dept (
    DeptID INT IDENTITY NOT NULL PRIMARY KEY,
    DeptName VARCHAR(50) NOT NULL,
    RaiseFactor NUMERIC(4, 2) 
)

CREATE TABLE dbo.Employee (
    EmployeeID INT IDENTITY NOT NULL PRIMARY KEY,
    DeptID INT FOREIGN KEY REFERENCES Dept,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    Salary NUMERIC(9,2) NOT NULL,
    PerformanceRating NUMERIC(4,2) NOT NULL,
    DateHire DATE NOT NULL,
    DatePosition DATE NOT NULL
)

INSERT dbo.Dept (DeptName, RaiseFactor)
VALUES ('Engineering', 1.2),
        ('Sales', .8),
        ('IT', 2.5),
        ('Manufacturing', 1.0) ;
INSERT dbo.Employee (
    DeptID, LastName, FirstName,
    Salary, PerformanceRating, DateHire, DatePosition)

VALUES (1, 'Smith', 'Sam', 54000, 2.0, '19970101', '19970101'),
        (1, 'Nelson', 'Slim', 78000, 1.5, '19970101', '19970101'),
        (2, 'Ball', 'Sally', 45000, 3.5, '19990202', '19990202'),
        (2, 'Kelly', 'Jeff', 85000, 2.4, '20020625', '20020625'),
        (3, 'Guelzow', 'Jo', 120000, 4.0, '19991205', '19991205'),
        (3, 'Ander', 'Missy', 95000, 1.8, '19980201', '19980201'),
        (4, 'Reagan', 'Sam', 75000, 2.9, '20051215', '20051215'),
        (4, 'Adams', 'Hank', 34000, 3.2, '20080501', '20080501');


SELECT EmployeeID, Salary,
CAST(CAST(DATEDIFF(d, DateHire, '20120625') AS DECIMAL(7, 2))
     / 365.25 AS INT) AS YrsCo,
CAST(CAST(DATEDIFF(d, DatePosition, '20120625') AS DECIMAL(7, 2))
     / 365.25 * 12 AS INT) AS MoPos,
CASE WHEN Employee.PerformanceRating >= 2
    THEN Employee.PerformanceRating
    ELSE 0
    END AS Perf,
    Dept.RaiseFactor
FROM dbo.Employee
JOIN dbo.Dept
ON Employee.DeptID = Dept.DeptID


SELECT EmployeeID, Salary,
    (2 + ((YearsCompany * .1) + (MonthPosition * .02)
    + (Performance * .5)) * RaiseFactor) / 100 AS EmpRaise
FROM 
    (SELECT EmployeeID, FirstName, LastName, Salary,
    CAST(CAST(DATEDIFF(d, DateHire, '20120625') AS
    DECIMAL(7, 2)) / 365.25 AS INT) AS YearsCompany,
    CAST(CAST(DATEDIFF(d, DatePosition, '20120625') AS
    DECIMAL(7, 2)) / 365.25 * 12 AS INT) AS MonthPosition,
    CASE WHEN Employee.PerformanceRating >= 2
    THEN Employee.PerformanceRating
    ELSE 0
    END AS Performance, Dept.RaiseFactor
    FROM dbo.Employee
    JOIN dbo.Dept
    ON Employee.DeptID = Dept.DeptID) AS SubQuery


SELECT EmployeeID, Salary,
    (2 +
    -- years with company
    + ((CAST(CAST(DATEDIFF(d, DateHire, '20120625')
    AS DECIMAL(7, 2)) / 365.25 AS INT) * .1)
    -- months in position
    + (CAST(CAST(DATEDIFF(d, DatePosition, '20120625')
    AS DECIMAL(7, 2)) / 365.25 * 12 AS INT) * .02)
    -- Performance Rating minimum
    + (CASE WHEN Employee.PerformanceRating >= 2
    THEN Employee.PerformanceRating
    ELSE 0
    END * .5))
-- Raise Factor
    * RaiseFactor) / 100 AS EmpRaise
FROM dbo.Employee
JOIN dbo.Dept
ON Employee.DeptID = Dept.DeptID

UPDATE Employee
SET Salary = Salary *
    (1 + ((2
    -- years with company
    + ((CAST(CAST(DATEDIFF(d, DateHire, '20120625')
    AS DECIMAL(7, 2)) / 365.25 AS INT) * .1)
    -- months in position
    + (CAST(CAST(DATEDIFF(d, DatePosition, '20120625')
    AS DECIMAL(7, 2)) / 365.25 * 12 AS INT) * .02)
    -- Performance Rating minimum
    + (CASE WHEN Employee.PerformanceRating >= 2
    THEN Employee.PerformanceRating
    ELSE 0
    END * .5)) * RaiseFactor) / 100 ))
FROM dbo.Employee
JOIN dbo.Dept
ON Employee.DeptID = Dept.DeptID

SELECT FirstName, LastName, Salary
FROM dbo.Employee


DROP TABLE dbo.Employee, dbo.Dept;