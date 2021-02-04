USE AdventureWorks2019
GO
SELECT DepartmentID, Name
FROM HumanResources.Department
ORDER BY DepartmentID
OFFSET 2 ROWS
FETCH NEXT 5 ROWS ONLY;


DECLARE @StartRow int = 1,
        @RowsPerPage int = 4
WHILE (SELECT count(*) FROM HumanResources.Department) >= @StartRow
BEGIN
    SELECT DepartmentID, Name
    FROM HumanResources.Department
    ORDER BY DepartmentID
    OFFSET @StartRow - 1 ROWS
    FETCH NEXT @RowsPerPage ROWS ONLY
    SET @StartRow = @StartRow + @RowsPerPage
END