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
   task 9

- SQL Server Bible <br />
	6, 7, 8, 9, 16, 17, 18, 44

<h3>Список</h3>

| !! | Тема | Короткий ответ
--- | ---  | --- 
!!  | GROUP BY  | группировка одинаковых значений, другие колонки аггрегируются SUM, MAX, AVG, MIN
!!  | CROSS JOIN  | декартово произведение или умножение одной таблицы на другую, каждая строка таблицы1 к каждой строке таблицы2
!!  | Основные JOIN's | FULL LEFT RIGHT OUTERS and INNER, картинка о пересечении кругов
!!  | DML  | (data manipulation lang) SELECT, INSERT, UPDATE, DELETE, MERGE часть синтаксиса для запросов и манипуляции данными в БД
!!  | DDL  | (data definition lang) CREATE, ALTER, DROP, TRUNCATE часть синтаксиса для управления структурой БД
!!  | DCL  | (data control lang) GRANT, REVOKE выдача/отзыв разрешений 
!!  | TCL  | (transaction control lang) COMMIT, SAVEPOINT, ROLLBACK, SET TRANSACTION, для управления транзакциями
!!  | Аггрегатные функции | (avg, sum, min, max) можем использовать при GROUP BY и при (sum, avg) на numeric, (min, max) not for bit
!!  | Set operators | (UNION EXCEPT, UNION ALL, INTERSECT) объединяет два запроса
!!  | Stored procedures | хранимые процедуры, запросы сохранённые отдельно, одинаковая производительность с adhoc
!!  | JOIN's vs UNION's | джоины добавляют столбцы по ключам (увеличивает горизонтально), юнионы объединяют запросы (увеличивает вертикльно)
!!  | Функции | scalar (возвращают одно значение BEGIN END RETURN), table inline (таблицу), multiple statement (таблицу, BEGIN END RETURN, declaring table structure, many statements)
!!  | APPLY | (CROSS APPLY, OUTER APPLY) декартово произведение, но на каждую строку можно применить функцию, cross возвращает значения, outer возвращает и NULL 
!!  | Подзапросы | скалярные (содержат одно значение столбца), коррелированные (зависят от внешнего подзапроса, рекурсивные)
!!  | CTE  | (common table expressions) иерархичные рекурсивные запросы
!!  | COUNT (*, 1, field) | нет разницы, использование 1 может выдавать некорректный результат
!!  | Windowed function | аналитические функции: row number (№ по порядку), rank (по порядку с 111446), dense rank (11222333), ntile(задаёшь количество мест)
!!  | PK, FK | pk ключ уникальный идентификатор строк, fk столбец - pk в другой таблице
!!  | Triggers | after (делаем что то после того как задет триггер), before = instead of (срабатывает триггер и делает что то, прежде чем выполнить операцию)
!!  | PIVOT, UNPIVOT | пивот - переводит строки в столбцы (группирует и меняет ось X на Y), анпивот - переводит столбцы в строки множит каждое бывшее название столбца на оставшийся столбец (разгруппировывает и меняет ось Y на X). Противоположны
!!  | CONSTRAINT | ограничения на столбец (NOT NULL, UNIQUE, PK, FK, CHECK specific condition, DEFAULT, INDEX)
!!  | OLAP, OLTP | online analytical processing (денормализованная), transactional (нормализованная)
!!  | ACID | Atomicity (транзакция проходит только полностью (до конца)), Consistency (согласует только допустимые результаты), Isolation (изолируется от других), Durability (транзакция долговечна, не должна быть отменена). Синтаксис TCL: COMMIT (сохраняем изменения), ROLLBACK (откатываем изменения), SAVEPOINT (точка сохранения), SET TRANSACTION (read only, read write)
!!  | data types | (money, datetime, datetime2, nvarchar UNICODE ASCII UTF-8
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


- индексы (B-tree структуры, кластерные/некластерные, конкретные колонки)
	balance tree
	leaf level
	doubled linked list
	pointer
	кучи
	complexity time
	fill factor
	page split
	index rebuild
	index maintenance
	репликации
	special type index
	covering indexes
	statistics
	
- temporary table, table variable (10 и более отличий, performance statistics)
- диалекты SQL https://en.wikipedia.org/wiki/SQL
- null and antinull standart
- теория множеств
- view, параметры (with scima bunding, with encrypt)
- materialized view
- ядро строит план выолнения запроса - 3 основных statement
- стадии выполнения запроса (логические, физические)
- MERGE в хранилищах OLAP - difference
- нормализация, денормализация (3 первых формы), OLTP хранилище
- селективность индексов (нужен ли индекс)
- property, ACID (read, commit, snapshot)
- transaction (выполняются или полностью или не выполняются, разобраться глубоко, долбить)
- phantom (как нарушение транзакций влияет на результаты, когда считывать данные)
- блокировака и deadlock
- performance
- операторы, запросы, performance
- разница performance (заменить что лучше что нельзя использовать)
