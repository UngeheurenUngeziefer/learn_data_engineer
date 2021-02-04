USE AdventureWorks2019

-- Merge Target Table
CREATE TABLE FlightPassengers
(
    FlightID INT NOT NULL IDENTITY PRIMARY KEY,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    FlightCode CHAR(6) NOT NULL,
    FlightDate DATE NOT NULL,
    Seat CHAR(3) NOT NULL
)

INSERT FlightPassengers
(LastName, FirstName, FlightCode, FlightDate, Seat)
VALUES
('LeBlanc', 'Patrick', 'SS2008', '20090301', '9F'),
('Jenkins', 'Sue', 'SS2008', '20090301', '7A'),
('Smith', 'Sam', 'SS2008', '20090301', '19A'),
('Nixon', 'Jerry', 'SS2008', '20090301', '29B')


-- Merge Source table
CREATE TABLE CheckIn
(
    LastName VARCHAR(50),
    FirstName VARCHAR(50),
    FlightCode CHAR(6),
    FlightDate DATE,
    Seat CHAR(3)
);
INSERT CheckIn
(LastName, FirstName, FlightCode, FlightDate, Seat)
VALUES 
('LeBlanc', 'Patrick', 'SS2008', '20090301', '9F'),
('Jenkins', 'Sue', 'SS2008', '20090301', '7A'),
('Nixon', 'Jerry', 'SS2008', '20090301', '2A'),
('Anderson', 'Missy', 'SS2008', '20090301', '4B')


-- NoShows
SELECT F.FirstName + ' ' + F.LastName AS Passenger, F.Seat
FROM FlightPassengers AS F
LEFT OUTER JOIN CheckIn AS C
    ON C.LastName = F.LastName
AND C.FirstName = F.FirstName
AND C.FlightCode = F.FlightCode
AND C.FlightDate = F.FlightDate
WHERE C.LastName IS NULL


-- Walk Up CheckIn
SELECT C.FirstName + ' ' + C.LastName AS Passenger, C.Seat
FROM CheckIn AS C
LEFT OUTER JOIN FlightPassengers AS F
ON C.LastName = F.LastName
AND C.FirstName = F.FirstName
AND C.FlightCode = F.FlightCode
AND C.FlightDate = F.FlightDate
WHERE F.LastName IS NULL


-- Seat Changes
SELECT C.FirstName + ' ' + C.LastName AS Passenger, 
        F.Seat AS 'previous seat', C.Seat AS 'final seat'
FROM CheckIn AS C
INNER JOIN FlightPassengers AS F
    ON C.LastName = F.LastName
AND C.FirstName = F.FirstName
AND C.FlightCode = F.FlightCode
AND C.FlightDate = F.FlightDate
AND C.Seat <> F.Seat
WHERE F.Seat IS NOT NULL


SELECT TOP(10) *
FROM FlightPassengers

SELECT TOP(10) *
FROM CheckIn


MERGE FlightPassengers F
USING CheckIn C
    ON C.LastName = F.LastName
AND C.FirstName = F.FirstName
AND C.FlightCode = F.FlightCode
AND C.FlightDate = F.FlightDate
WHEN Matched

THEN UPDATE
SET F.Seat = C.Seat
WHEN NOT MATCHED BY TARGET
THEN INSERT (FirstName, LastName, FlightCode, FlightDate, Seat)
VALUES (FirstName, LastName, FlightCode, FlightDate, Seat)
WHEN NOT MATCHED BY SOURCE
THEN DELETE;

SELECT FlightID, FirstName, LastName, FlightCode, FlightDate, Seat
FROM FlightPassengers