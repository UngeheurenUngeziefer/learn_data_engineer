<h3>Data Integration DB and ETL</h3>

!!- sqlbolt
!!- learndb
!!- onboarding (completed) (100%)
!!- english (completed) (writing B1, speaking B1)
!!- Developing Miscrofot SQL Server 2016 Databases (completed)
!!- SQL Server 2016: Provision a Database (completed)

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
- task 8 <br />
	1, 2, 3

- SQL Server Bible <br />
	6, 7, 8, 9, 16, 17, 18, 

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


!- multistatement пройти
!- функции (скалярные, table inline, inline, multiple statement) <br />

!- JOIN's vs UNION's <br />
!- APPLY (CROSS OUTER) <br />
!- GROUP BY vs HAVING
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


!- подзапросы (скалярные, коррелированные) vs CTE (common table expressions) - difference  <br />
!- COUNT (*, 1, field) - there is no difference (1 не юзать) <br />
!- window function (аналитические функции), (row number, rank, dense rank) <br />
!- Primary Key, Foreign Key - хорошо знать разницу, и что это <br />

- temporary table, table variable (10 и более отличий, performance statistics)
~ CONSTRAINT (PK, not now)
- диалекты SQL https://en.wikipedia.org/wiki/SQL

- PIVOT, UNPIVOT
- null and antinull standart
- теория множеств

~ view, параметры (with scima bunding, with encrypt)
- materialized view
- trigger как в salesforce

- ядро строит план выолнения запроса - 3 основных statement
- стадии выполнения запроса (логические, физические)
- set operators
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