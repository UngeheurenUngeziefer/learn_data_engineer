DECLARE @B INT, @Q INT
SET @B = 2007
SET @Q = 25

SELECT
    CASE 
        WHEN @B = 2007 
            AND @Q BETWEEN 20 AND 30
        THEN 1
        ELSE NULL
    END AS Test
