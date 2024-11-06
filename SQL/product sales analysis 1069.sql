-- (sale_id, year) is the primary key (combination of columns with unique values) of this table.
-- product_id is a foreign key (reference column) to Product table.
-- Each row of this table shows a sale on the product product_id in a certain year.
-- Note that the price is per unit. product_name | year  | price 

select product_name , year  , price from Sales  LEFT JOIN  Product on Sales.sale_id = Product.product_id order by year asc;

select Product.product_name , Sales.year  , Sales.price 
from Sales
LEFT JOIN  Product on Sales.product_id = Product.product_id;