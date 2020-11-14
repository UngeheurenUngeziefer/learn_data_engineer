USE AdventureWorks2019
SELECT Name AS 'Product_Name',
        SellStartDate + 365 One_Year_Sell_Start_Date
FROM Production.Product;