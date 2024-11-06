use classicmodels;


describe orders ;
describe customers;

describe employees;

select * from customers;


select customerName as Name, city as Town,country,phone from customers;

select customerName , city,country,phone from customers;

select 1+1;

select now();

select concat('naimur',' ','rahman') as Name;



SELECT employeeNumber as ID,CONCAT(firstName, ' ', lastName) AS Name, email AS Email ,officeCode,jobTitle as Title
FROM employees 
ORDER BY officeCode asc,employeeNumber asc;


SELECT employeeNumber as ID,CONCAT(firstName, ' ', lastName) AS Name, email AS Email ,officeCode,jobTitle as Title
FROM employees 
ORDER BY officeCode * employeeNumber asc;



SELECT FIELD('C', 'A', 'B','C');

select * from orders;


select orderNumber,status from orders order by field(status, 'In Process', 
    'On Hold', 
    'Cancelled', 
    'Resolved', 
    'Disputed', 
    'Shipped');
    
    
select firstName,lastName,reportsTo from employees order by reportsTo desc;


SELECT 
    lastname, 
    firstname, 
    jobtitle
FROM
    employees
WHERE
    jobtitle = 'Sales Rep';


SELECT 
    lastname, 
    firstname, 
    jobtitle
FROM
    employees
WHERE
    jobtitle = 'Sales Rep' and officeCode = 1;
    
show databases;
use classicmodels;

select lastName,firstName,jobTitle,officeCode from employees where jobtitle = 'Sales Rep' or officeCode = 1 order by officeCode,jobTitle;

select lastName,firstName,officeCode from employees where officeCode between 1 and 2 order by officeCode,jobTitle;

SELECT 
    e.lastName, 
    e.firstName, 
    e.officeCode,
    (SELECT COUNT(*) 
     FROM employees 
     WHERE officeCode BETWEEN 1 AND 2) AS employeeCount
FROM employees e
WHERE e.officeCode BETWEEN 1 AND 2
ORDER BY e.officeCode, e.jobTitle;


select concat(firstName,' ', lastName) as Name from employees where lastName like '%son' order by firstName;

select firstName,lastName,officeCode 
from employees 
where  officeCode in (1,2,3)
order by officeCode desc;

select lastName,firstName,reportsTo
From employees 
where reportsTo is null;



SELECT 
    lastname, 
    firstname, 
    jobtitle
FROM
    employees
WHERE
    jobtitle <> 'Sales Rep';
    


SELECT 
    lastname, 
    firstname, 
    officeCode
FROM
    employees
WHERE 
    officecode >= 5 order by officeCode asc;
    
    
SELECT 
    lastname as LastName
FROM
    employees
ORDER BY 
    lastname;
    
    
SELECT DISTINCT state,city
FROM customers;

SELECT DISTINCT
    state, city
FROM
    customers
WHERE
    state IS NOT NULL
ORDER BY 
    state, 
    city;


SELECT 1 AND 0, 0 AND 1, 0 AND 0, 0 AND NULL;

SELECT 1 = 0 AND 1 / 0 ;

SELECT 
    customername, 
    country, 
    state
FROM
    customers
WHERE
    country = 'USA' AND 
    state = 'CA';
    

SELECT 
    customername, 
    country, 
    state, 
    creditlimit
FROM
    customers
WHERE
    country = 'USA' AND 
    state = 'CA' AND 
    creditlimit > 100000;
    
SELECT NULL NOT IN (1,2,3);

SELECT 
    officeCode, 
    city, 
    phone,
    country
FROM
    offices
WHERE
    country NOT IN ('USA' , 'UK')
    
ORDER BY 
    city;
    
    
SELECT 2 BETWEEN 20 AND 300;

SELECT 15 NOT BETWEEN 10 AND 30;

SELECT 
    productCode, 
    productName, 
    buyPrice
FROM
    products
WHERE
    buyPrice BETWEEN 90 AND 100 order by buyPrice desc;
    
SELECT 
    productCode, 
    productName, 
    buyPrice
FROM
    products
WHERE
    buyPrice  NOT BETWEEN 20 AND 100 order by buyPrice;
    
SELECT 
    productCode, 
    productName, 
    buyPrice
FROM
    products
WHERE
    buyPrice < 20 OR buyPrice > 100;
    
SELECT 
   orderNumber,
   requiredDate,
   status
FROM 
   orders
WHERE 
   requireddate BETWEEN 
     CAST('2003-01-01' AS DATE) AND 
     CAST('2003-01-31' AS DATE);
     
SELECT 
    employeeNumber, 
    lastName, 
    firstName
FROM
    employees
WHERE
    firstName LIKE 'a%';

SELECT 
    employeeNumber, 
    lastName, 
    firstName
FROM
    employees
WHERE
    lastName LIKE '%on';


SELECT 
    employeeNumber, 
    lastName, 
    firstName
FROM
    employees
WHERE
    lastname LIKE '%on%';
    
SELECT 
    employeeNumber, 
    lastName, 
    firstName
FROM
    employees
WHERE
    firstname LIKE 'T_m';
    
SELECT 
    employeeNumber, 
    lastName, 
    firstName
FROM
    employees
WHERE
    lastName NOT LIKE 'B%';
    
SELECT 
    productCode, 
    productName
FROM
    products
WHERE
    productCode LIKE '%\_20%';
    
SELECT 
    customerNumber, 
    customerName, 
    creditLimit
FROM
    customers
ORDER BY creditLimit DESC
LIMIT 5;


SELECT 
    customerNumber, 
    customerName, 
    creditLimit
FROM
    customers
ORDER BY creditLimit DESC
LIMIT 5;


SELECT 
    customerNumber, 
    customerName
FROM
    customers
ORDER BY customerName    
LIMIT 10, 10;


SELECT 
    customerName, 
    creditLimit
FROM
    customers
ORDER BY 
    creditLimit DESC    
LIMIT 1,1;

SELECT DISTINCT
    state
FROM
    customers
WHERE
    state IS NOT NULL
LIMIT 5;


SELECT 
    customerName, 
    country, 
    salesrepemployeenumber
FROM
    customers
WHERE
    salesrepemployeenumber IS  NULL
ORDER BY 
    customerName;
    
SELECT
   CONCAT_WS(', ', lastName, firstname) AS `Full name`
FROM
   employees;
   
SELECT
	orderNumber `Order no.`,
	SUM(priceEach * quantityOrdered) Total
FROM
	orderdetails
GROUP BY
	`Order no.`
HAVING
	total > 60000;
    



SELECT * FROM employees e;


SELECT
	customerName FullName,
	COUNT(o.orderNumber) total
FROM
	customers c
INNER JOIN orders o ON c.customerNumber = o.customerNumber 
group by customerName;


SELECT
	customers.customerName,
	COUNT(orders.orderNumber) total
FROM
	customers
INNER JOIN orders ON customers.customerNumber = orders.customerNumber
GROUP BY
	customerName
ORDER BY
	total DESC;
    
    
    
    
    
    
    
CREATE TABLE members (
    member_id INT AUTO_INCREMENT,
    name VARCHAR(100),
    PRIMARY KEY (member_id)
);
    
describe members;
select * from members;


CREATE TABLE committees (
    committee_id INT AUTO_INCREMENT,
    name VARCHAR(100),
    PRIMARY KEY (committee_id)
);


INSERT INTO members(name)
VALUES('John'),('Jane'),('Mary'),('David'),('Amelia');

INSERT INTO committees(name)
VALUES('John'),('Mary'),('Amelia'),('Joe');

select * from members; 
    
    
    
select members.member_id,members.name as Member, committees.committee_id,committees.name Commitee
from members inner join committees on committees.name = members.name;


SELECT 
    m.member_id, 
    m.name AS member, 
    c.committee_id, 
    c.name AS committee
FROM
    members m
INNER JOIN committees c USING(name);


SELECT 
    m.member_id, 
    m.name AS member, 
    c.committee_id, 
    c.name AS committee
FROM
    members m
LEFT JOIN committees c USING(name);

SELECT 
    m.member_id, 
    m.name AS member, 
    c.committee_id, 
    c.name AS committee
FROM
    committees c
LEFT JOIN members m USING(name);


SELECT 
    m.member_id, 
    m.name AS member, 
    c.committee_id, 
    c.name AS committee
FROM
    members m
RIGHT JOIN committees c on c.name = m.name;


SELECT 
    m.member_id, 
    m.name AS member, 
    c.committee_id, 
    c.name AS committee
FROM
    members m
RIGHT JOIN committees c USING(name)
WHERE m.member_id IS NULL;


SELECT 
    m.member_id, 
    m.name AS member, 
    c.committee_id, 
    c.name AS committee
FROM
    members m
CROSS JOIN committees c;

SELECT 
    productCode Code, 
    productName ProductName, 
    textDescription
FROM
    products t1
INNER JOIN productlines t2 
    ON t1.productline = t2.productline;
    
    
    


SELECT 
    orderNumber,
    orderDate,
    orderLineNumber,
    productName,
    quantityOrdered,
    priceEach
FROM
    orders
INNER JOIN
    orderdetails USING (orderNumber)
INNER JOIN
    products USING (productCode)
ORDER BY 
    orderNumber asc, 
    priceEach asc,
    orderLineNumber asc;
    

select * from products;

SELECT 
    orderNumber,
    orderDate,
    customerName,
    orderLineNumber,
    productName,
    quantityOrdered,
    priceEach
FROM
    orders
INNER JOIN orderdetails 
    USING (orderNumber)
INNER JOIN products 
    USING (productCode)
INNER JOIN customers 
    USING (customerNumber)
ORDER BY 
    orderNumber, 
    orderLineNumber;
    
    


SHOW DATABASES;

CREATE DATABASE testdb;
show databases; 


DROP DATABASE testdb;

SELECT database();


SELECT 
    lastName, firstName
FROM
    employees
WHERE
    officeCode IN (SELECT 
            officeCode
        FROM
            offices
        WHERE
            country = 'USA');
            
SELECT 
    customerNumber, 
    checkNumber, 
    amount
FROM
    payments
WHERE
    amount = (SELECT MAX(amount) FROM payments);
    
SELECT 
    customerName
FROM
    customers
WHERE
    customerNumber NOT IN (SELECT DISTINCT
            customerNumber
        FROM
            orders);


CREATE TABLE sales
SELECT
    productLine,
    YEAR(orderDate) orderYear,
    SUM(quantityOrdered * priceEach) orderValue
FROM
    orderDetails
        INNER JOIN
    orders USING (orderNumber)
        INNER JOIN
    products USING (productCode)
GROUP BY
    productLine ,
    YEAR(orderDate);


SELECT * FROM sales;

SELECT 
    productline, 
    SUM(orderValue) totalOrderValue
FROM
    sales
GROUP BY 
    productline;
