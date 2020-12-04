USE AdventureWorks2019

GO
UPDATE Address
SET County = REPLACE(County, 'Sun', 'Dark')
WHERE County LIKE '%Shine'


SELECT County FROM Address
WHERE County LIKE '%Shine'