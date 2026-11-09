USE northwind; 
-- 1 List the product id, product name, unit price and category name of all products.
-- Order by category name and within that, by product name. 
SELECT productid, productname, unitprice, categoryname 
FROM products  
JOIN categories ON products.categoryid = categories.categoryid
ORDER BY categoryname, productname; 
-- 2  List the product id, product name, unit price and supplier name of all products that cost more than $75. 
-- Order by product name. 
SELECT productid, productname, unitprice, companyname 
FROM products 
JOIN suppliers ON products.supplierid = suppliers.supplierid 
WHERE unitprice > 75
ORDER BY productname; 
-- 3 List the product id, product name, unit price, category name, and supplier name of every product. 
-- Order by product name. 
SELECT productid, productname, unitprice, categoryname, companyname 
FROM products 
JOIN categories ON products.categoryid = categories.categoryid 
JOIN suppliers ON products.supplierid = suppliers.supplierid 
ORDER BY productname; 
-- 4 List the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. 
-- Assign the shipping company name the alias ‘Shipper.’ 
--  Order by the name of the shipper, then the name of who it shipped to. 
SELECT orderid, shipname, shipaddress, shippers.companyname AS shipper 
FROM orders 
JOIN shippers ON orders.shipvia = shippers.shipperid
WHERE shipcountry = 'Germany' 
ORDER BY shipper, shipname; 
-- 5 Start from the same query as above (#4), but omit OrderID and add logic to group by ship name. 
-- count of how many orders were shipped for that ship name. 
SELECT shipname, shipaddress, shippers.companyname AS shipper, COUNT(*) AS ordercount
FROM orders 
JOIN shippers ON orders.shipvia = shippers.shipperid
WHERE shipcountry = 'Germany' 
GROUP BY shipname, shipaddress, shippers.companyname 
ORDER BY shipper, shipname; 
-- 6 List the order id, order date, ship name, ship address of all
-- orders that included Sasquatch Ale. 
SELECT orders.orderid, orderdate, shipname, shipaddress 
FROM orders 
JOIN `order details` ON orders.orderid = `order details`.orderid 
JOIN products ON `order details`.productid = products.productid 
WHERE productname = 'Sasquatch Ale';