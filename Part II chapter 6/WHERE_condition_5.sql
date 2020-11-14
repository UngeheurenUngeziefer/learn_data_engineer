USE AdventureWorks2019
SELECT StateProvinceCode
    FROM Person.StateProvince
    WHERE StateProvinceCode NOT IN ('NC', 'WV');