-- value of true if either input is true, but not if both are true
SELECT 1 ^ 1 AS both_true,
       1 ^ 0 AS one_true,
       3 ^ 5 AS decimal_six
