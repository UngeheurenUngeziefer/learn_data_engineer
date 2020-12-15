Data Integration DB and ETL
	
!- onboarding (passed) (OK)
!- english (passed) (B1)
	- writing (passed) (B1)
	- speaking (passed) (B1)
!- cloud preparing docs completed
- SQL Server Bible
	!- chapter 6 ----------------------------------------------|
		- Start info, installation, history
		- Comparison Operators, WHERE, BETWEEN
		- IN, SOME, ANY, ALL
		- LIKE, NOT, AND, OR
		- ALL, DISTINCT
		- Collations
		- ORDER BY
		- Random row
		- TOP, WHERE, WITH TIES
	!- chapter 7 ----------------------------------------------|
		- db design phases
		- normalization
		- generalization
		- rules of one
		- PK and FK
		- design patterns
			- one-to-one, one-to-many, many-to-many
			- supertype/subtype
			- domain integrity lookup
			- recursive pattern (one-to-many, many-to-many)
			- entity-value pairs pattern
		- db design layers
		- normal forms (1, 2, 3, 4, 5, BCNF)
		- strategy considerations
	!- chapter 8 ----------------------------------------------|
		- datatypes
			- character
			- numeric
			- datetime
			- other
		- building expressions
			- addition
			- ceiling, modulo, floor, concat, dividing
			- bitwise operators
			- null, case, coalesce, iif, isnull
		- scalar functions
			- user info funcs
			- datetime funcs
	!- chapter 9 ----------------------------------------------|
		- JOIN's
			- INNER JOIN's
			- OUTER JOIN's
			- SELF JOIN's
			- CROSS JOIN's
		- View's
			- CREATE
			- ALTER
			- DROP
		- Column Aliases
		- ORDER BY
		- Newsted Views, Synonyms, protecting, uchecked
		- INSERT, ALTER, DROP, CREATE
	- chapter 16 ---------------------------------------------|
		- IF ELSE
		- IF EXISTS
		- Variables
		- Batches
		- Errors
		- Fetch and Offset
		- system funcs
		- while loop
	- chapter 17 ---------------------------------------------|

!- module 1 (passed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9
!- module 2 (passed) <br />
	1, 2, 3, 4, 5, 6, 7
!- module 3 (passed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9, 10
!- module 4 (passed) <br />
	1, 2, 3, 4, 5, 6, 7, 8
!- module 5 (sended) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9



Список:
!- CROSS JOIN (декартово произведение или умножение одной таблицы на другую, каждая строка таблицы1 к каждой строке таблицы2) 
!- другие JOIN's (вспоминаем картинку) FULL LEFT RIGHT OUTERS and INNER
!~ UNION EXCEPT, UNION ALL, INTERSECT (объединяет два запроса, редко юзается)
!~ COUNT (*, 1, field) - there is no difference (1 не юзать)
!- подзапросы (скалярные, коррелированные, CTE(common table expressions)) - difference
!- window function (аналитические функции), (row number, rank, dense rank)
!- GROUP BY 
!- аггрегатные функции (average, sum, min, max) - когда мы можем их использовать
!~ Primary Key, Foreign Key - хорошо знать разницу, и что это
!~ функции (скалярные, inline, multiple statement)
!- APPLY (CROSS, OUTER)

!!- DML (CREATE, UPDATE, INSERT, DELETE) (data manipulation lang)
!!- DDL (CREATE, ALTER, DROP) (data definition lang), 
!!- DCL (data control lang)
!!- TCL (transaction control lang)

V- необходимо прочитать главы II, IV, VIII книги Microsoft SQL Server 2012 Bible)
	!- II
	V- IV
	- VIII
- null and antinull standart

- теория множеств
- set operators
- стадии выполнения запроса (логические, физические)
- ядро строит план выолнения запроса - 3 основных statement
- PIVOT, UNPIVOT
- MERGE в хранилищах OLAP - difference
- trigger как в salesforce
- нормализация, денормализация (3 первых формы), OLTP хранилище
- OLAP, OLTP
~ CONSTRAINT (PK, notnow)
- индексы (B-tree структуры, кластерные/некластерные, конкретные колонки)
- performance
- селективность индексов (нужен ли индекс)
~ view, параметры (with scima bunding, with encrypt)
- materialized view
- разница performance (заменить что лучше что нельзя использовать)
- transaction (выполняются или полностью или не выполняются, разобраться глубоко, долбить)
- property, ACID (read, commit, snapshot)
- phantom (как нарушение транзакций влияет на результаты, когда считывать данные)
- блокировака и deadlock
- temporary table, table variable (10 и более отличий, performance statistics)
- операторы, запросы, performance
