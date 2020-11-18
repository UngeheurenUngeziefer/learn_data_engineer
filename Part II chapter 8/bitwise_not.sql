DECLARE @A BIT
SET @A = 1
SELECT ~@A AS not_a,
       @A AS real_a
