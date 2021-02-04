USE AdventureWorks2019;
SELECT Name
FROM Person.StateProvince
WHERE StateProvinceCode = 'NC'
OR StateProvinceCode = 'WV';