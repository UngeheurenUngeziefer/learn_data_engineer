USE AdventureWorks2019

MERGE FlightPassengers F
USING CheckIn C
    ON C.LastName = F.LastName
    AND C.FirstName = F.FirstName
    AND C.FlightCode = F.FlightCode
    AND C.FlightDate = F.FlightDate
WHEN MATCHED
THEN UPDATE
SET F.Seat = C.Seat
WHEN NOT MATCHED BY TARGET
THEN INSERT (FirstName, LastName, FlightCode, FlightDate, Seat)
VALUES (FirstName, LastName, FlightCode, FlightDate, Seat)
WHEN NOT MATCHED BY SOURCE
THEN DELETE
OUTPUT deleted.FlightID, deleted.LastName, Deleted.Seat, $action,
    inserted.FlightID, inserted.LastName, inserted.Seat;