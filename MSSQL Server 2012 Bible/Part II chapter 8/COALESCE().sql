-- return the dirst non null value
SELECT COALESCE(NULL, 1+NULL, 1+2, 'abc') AS non_null_val;
