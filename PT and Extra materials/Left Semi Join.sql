USE TestSQL
-- convert left joins to inner join
CREATE TABLE First_table 
(
	id INT PRIMARY KEY IDENTITY(1,1),
	first_name VARCHAR(50)
)
INSERT INTO First_table(first_name)
VALUES('Alex')
INSERT INTO First_table(first_name)
VALUES('John')
INSERT INTO First_table(first_name)
VALUES('Mary')
INSERT INTO First_table(first_name)
VALUES('Vova')
INSERT INTO First_table(first_name)
VALUES('Ann')

CREATE TABLE Second_table
(
	id INT,
	last_name VARCHAR(50),
	--FOREIGN KEY(id) REFERENCES First_table(id)
)
INSERT INTO Second_table(id, last_name)
VALUES(1, 'Utterson')
INSERT INTO Second_table(id, last_name)
VALUES(2, 'Smith')
INSERT INTO Second_table(id, last_name)
VALUES(3, 'Korolev')
INSERT INTO Second_table(id, last_name)
VALUES(4, 'Pupkin')

SELECT * FROM First_table		-- 5 rows
SELECT * FROM Second_table		-- 4 rows


SELECT *						-- 4 rows				
FROM First_table frs
INNER JOIN Second_table sec
ON frs.id = sec.id

SELECT *						-- 5 rows with NULL's from second table		
FROM First_table frs
LEFT OUTER JOIN Second_table sec
ON frs.id = sec.id



;WITH cte1 AS
(
	SELECT id, first_name
	FROM First_table f
	WHERE id NOT IN
	(
		SELECT id
		FROM Second_table s
	)
), cte2 AS 
(
	SELECT *, NULL AS last_name_name
	FROM cte1
)

SELECT f.id, first_name, s.last_name
FROM First_table f
INNER JOIN Second_table s
ON f.id = s.id
UNION
SELECT * FROM cte2