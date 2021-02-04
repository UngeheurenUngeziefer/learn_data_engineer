USE AdventureWorks2019
BEGIN TRY
	BEGIN TRANSACTION
		UPDATE Production.ProductInventory
		SET Quantity -= 100
		WHERE ProductID = 527
		AND LocationID = 6					-- misc storage
		AND Shelf = 'B'
		AND Bin = 4;
		UPDATE Production.ProductInventory
		SET Quantity += 100
		WHERE ProductID = 527
		AND LocationID = 50					-- subassembly area
		AND Shelf = 'F'
		AND Bin = 11;
	COMMIT TRANSACTION;
END TRY
BEGIN CATCH
IF Xact_State() = 1                     -- there's an active committable transaction
COMMIT TRAN;
IF Xact_State() = -1                    -- there's an uncommittable transaction
BEGIN
ROLLBACK TRANSACTION;
RAISERROR('Inventory Transaction Error', 16, 1);
END
END CATCH;