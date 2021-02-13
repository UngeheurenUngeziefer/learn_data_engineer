<h3>Data Integration DB and ETL</h3>

!!- sqlbolt
!!- learndb
!!- onboarding (100%)
!!- english (writing B1, speaking B1)
!!- Developing Miscrofot SQL Server 2016 Databases
!!- SQL Server 2016: Provision a Database
!!- Advanced SQL for Query Tuning and Performance Optimization
!!- Optimize query performance in SQL Server
!!- task 1 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9
!!- task 2 (completed) <br />
	1, 2, 3, 4, 5, 6, 7
!!- task 3 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9, 10
!!- task 4 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8
!!- task 5 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9
!!- task 6 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
!!- task 7 (completed) <br />
	1, 2, 3, 4 
!!- task 8 (completed) <br />
	1, 2, 3, 4
!!- task 9 (completed) <br />
	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
!!- SQL Server Bible <br />
	6, 7, 8, 9, 16, 17, 18, 44, 45, 46, 47, 48, 49, 50
!!- Articles
	1, 2
!!- Kudvenkat
	transactions: isolations lvls, concurrency
!!- SQL Server Performance for Developers
!!- Interview 1 f

!- DB Knowledge Assesment
	1, 2

!- Interview 2
	speech, research

!- Azure Data Factory
	1, 2, 3, 4, 5

!- TPCH



	
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
!!  | data types | выбирать наименьший типа данных, например varcharmax займёт сразу 2ГБ вне зависимости от того, сколько символов ты введёшь, сортировка только по int, не использовать text умирает и не эффективно, char только если все значения фиксированной длины, использовать datetime2 а не datetime, избегать экзотику money, geolocations (только если строго необходимо), не использовать UDF, не использовать float, datetime, real как PK
!!  | индексы | B-tree структура, кластерные/некластерные, на конкретные колонки, нужно не много и не мало, влияют на performance, кластерные строки упорядочены по значению ключа индекса, если нет кластерного то это куча, некластерный индекс имеет поинтеры на записи. Кластерный один, некластерных много 
!! | leaf level | самый низкий уровень индекса, содержит значение ключа для каждой строки в таблице
!! | complexity time | complexity and time of algorithm n O
!! | fill factor | proporion of space used in a db index, the rest being reserved
!! | page split | the process of moving half the rows or entries in a full data or index page to a new page to make room for a new row or index entry
!! | index rebuild | При перестроении индекса он удаляется и создается заново. Это устраняет фрагментацию, освобождает дисковое пространство путем сжатия страниц на основе указанного или существующего параметра fill factor и переупорядочивает строки индекса на смежных страницах
!! | репликации | Репликация MS SQL позволяет создать точную копию бд в другом месте (на другом сервере). Для MS SQL репликация данных решает множество задач, от зеркалирования базы до создания тестовой версии набора данных.
!! | special type index | unique (уникальность каждой строки), full-text (эффективный поиск слов в строковых данных), spatial (это облегчает возможность эффективного выполнения операций с пространственными объектами), filtered (некластеризованный индекс. Полностью оптимизирован для запроса данных из четко определенного набора данных. Фильтр используется для определения части строк в таблице, подлежащих индексации)
!! | covering index | может удовлетворить все запрошенные столбцы в запросе без выполнения дальнейшего поиска в кластеризованном индексе
!! | statistics | оптимизатор запросов использует статистику для создания планов запросов, которые повышают производительность запросов.	


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


trace flag
count stored indexes
column stored indexes
null antinull standart
view, параметры (with scima bunding, with encrypt)
materialized view
ядро строит план выолнения запроса - 3 основных statement
стадии выполнения запроса (логические, физические)
MERGE в хранилищах OLAP - difference`
нормализация, денормализация (3 первых формы), OLTP хранилище
селективность индексов (нужен ли индекс)
property, ACID (read, commit, snapshot)
phantom (как нарушение транзакций влияет на результаты, когда считывать данные)
блокировака и deadlock


