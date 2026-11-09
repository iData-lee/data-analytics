USE northwind; 
-- 1  Product name(s) of the most expensive products 
SELECT productname, unitprice
FROM products
WHERE unitprice = (SELECT MAX(unitprice) 
FROM products); 
-- 2 The product name(s) and categories of the least expensive products
SELECT p.productname, c.categoryname 
FROM products p 
JOIN categories c ON p.categoryid = c.categoryid
WHERE p.unitprice = (SELECT MIN(unitprice) 
FROM products); 
--  3 The order id, shipping name and shipping address of all orders shipped via "Federal Shipping"
SELECT orderid, shipname, shipaddress 
FROM orders
WHERE shipvia = (SELECT shipperid FROM shippers WHERE companyname = 'Federal Shipping'); 
-- 4 The order ids of the orders that included "Sasquatch Ale" 
SELECT orderid 
FROM `order details`
WHERE productid = (SELECT productid FROM products 
WHERE productname = 'Sasquatch Ale');
-- 5 Name of the employee that sold order 10266
SELECT firstname, lastname 
FROM employees 
WHERE employeeid = (SELECT employeeid FROM orders 
WHERE orderid = 10266); 
--  6 Name of the customer that bought order 10266 
SELECT companyname 
FROM customers 
WHERE customerid = (SELECT customerid FROM orders
WHERE orderid = 10266);
