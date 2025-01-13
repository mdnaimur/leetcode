SELECT 
    p.student_id,
    p.student_name,
    s.subject_name,
  count(e.student_id) AS attended_exams
FROM 
    students p
cross JOIN 
    subjects s 
left JOIN 
    Examinations e 
ON 
    p.student_id = e.student_id
and 
    s.subject_name = e.subject_name
    
GROUP BY 
    p.student_id, p.student_name, s.subject_name
ORDER BY 
    p.student_id, s.subject_name;
