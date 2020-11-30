USE AdventureWorksLT2019

SELECT Name as ProductName
  FROM SalesLT.Product
 WHERE ProductID IN
    (SELECT ProductID
       FROM SalesLT.SalesOrderDetail
      WHERE SalesOrderID IN
        (SELECT SalesOrderID -- Find the Orders with vests
           FROM SalesLT.SalesOrderDetail
          WHERE ProductID IN
            (SELECT ProductID
               FROM SalesLT.Product
              WHERE ProductCategoryID =
                -- 1. Find the Vests category
                (Select ProductCategoryID
                   FROM SalesLT.ProductCategory
                  WHERE NAME = 'Vests' ) ) ) );