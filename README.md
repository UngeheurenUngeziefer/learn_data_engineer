<h3>Data Integration DB and ETL</h3>

!!- sqlbolt
!!- learndb
!!- onboarding (100%)
!!- english (writing B1, speaking B1)
!!- Developing Miscrofot SQL Server 2016 Databases
!!- SQL Server 2016: Provision a Database

!- task 1 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9
!- task 2 (completed) <br />
	1, 2, 3, 4, 5, 6, 7
!- task 3 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9, 10
!- task 4 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8
!- task 5 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9
!- task 6 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
!- task 7 (completed) <br />
	1, 2, 3, 4 
!- task 8 (completed)<br />
	1, 2, 3, 4

- SQL Server Bible <br />
	6, 7, 8, 9, 16, 17, 18

Список:
!!- GROUP BY (когда можно использовать)
!!- CROSS JOIN (декартово произведение или умножение одной таблицы на другую, каждая строка таблицы1 к каждой строке таблицы2) <br />
!!- другие JOIN's (вспоминаем картинку) FULL LEFT RIGHT OUTERS and INNER <br />
!!- DML (CREATE, UPDATE, INSERT, DELETE) (data manipulation lang) <br />
!!- DDL (CREATE, ALTER, DROP) (data definition lang) <br />
!!- DCL (data control lang) <br />
!!- TCL (transaction control lang) <br />
!!- аггрегатные функции (average, sum, min, max) - когда мы можем их использовать <br />
!!- UNION EXCEPT, UNION ALL, INTERSECT (объединяет два запроса, редко юзается) <br />
!!- stored procedures
!- JOIN's vs UNION's <br />
!- функции (скалярные, table inline, inline, multiple statement) <br />
!- multistatement
!- APPLY (CROSS OUTER) <br />
!- GROUP BY vs HAVING
!- подзапросы (скалярные, коррелированные) vs CTE (common table expressions) - difference  <br />
!- COUNT (*, 1, field) - there is no difference (1 не юзать) <br />
!- window function (аналитические функции), (row number, rank, dense rank) <br />
!- Primary Key, Foreign Key - хорошо знать разницу, и что это <br />
!- triggers (after, before = instead of)
!- PIVOT, UNPIVOT
!- CONSTRAINT (PK, not now)
!- set operators

!- data types (money, datetime, datetime2, nvarchar UNICODE ASCII UTF-8
	UDF types https://www.mssqltips.com/sqlservertip/4100/how-to-find-udfs-causing-sql-server-performance-issues/
	SP,
	принципы работы с типами данных:
		- выбирать наименьший типа данных (если нужно только 9 цифр использовать 9 для оптимизации)
		  например varcharmax займёт сразу 2ГБ вне зависимости от того, сколько символов ты введёшь
		- varchar(50) если не уверен 
		- сортировка только по int
		- не использовать text умирает и не эффективно
		- char только если все значения фиксированной длины
		- использовать datetime2 а не datetime
		- избегать экзотику money, geolocations (только если строго необходимо)
		- не использовать UDF
		- не использовать float, datetime, real как PK

- temporary table, table variable (10 и более отличий, performance statistics)
- диалекты SQL https://en.wikipedia.org/wiki/SQL
- null and antinull standart
- теория множеств
- view, параметры (with scima bunding, with encrypt)
- materialized view
- ядро строит план выолнения запроса - 3 основных statement
- стадии выполнения запроса (логические, физические)
- MERGE в хранилищах OLAP - difference
- OLAP, OLTP
- нормализация, денормализация (3 первых формы), OLTP хранилище
- индексы (B-tree структуры, кластерные/некластерные, конкретные колонки)
- селективность индексов (нужен ли индекс)
- property, ACID (read, commit, snapshot)
- transaction (выполняются или полностью или не выполняются, разобраться глубоко, долбить)
- phantom (как нарушение транзакций влияет на результаты, когда считывать данные)
- блокировака и deadlock
- performance
- операторы, запросы, performance
- разница performance (заменить что лучше что нельзя использовать)
