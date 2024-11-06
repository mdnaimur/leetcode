

select Visits.customer_id , count(Transactions.transaction_id) as count_no_trans 
 from Visits 
 right join Transactions on Visits.visit_id = Transactions.visit_id
 GROUP BY Visits.customer_id;


 select Visits.customer_id , count(Visits.visit_id) as count_no_trans 
 from Visits 
 left  join Transactions on Visits.visit_id = Transactions.visit_id
 WHERE Transactions.transaction_id IS NULL 
  GROUP BY Visits.customer_id;

SELECT customer_id, COUNT(visit_id) as count_no_trans 
FROM Visits
WHERE visit_id NOT IN (
	SELECT visit_id FROM Transactions
	)
GROUP BY customer_id

SELECT customer_id, COUNT(visit_id) as count_no_trans 
FROM Visits v
WHERE NOT EXISTS (
	SELECT visit_id FROM Transactions t 
	WHERE t.visit_id = v.visit_id
	)
GROUP BY customer_id