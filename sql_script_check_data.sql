-- see data in each table

select * from tblStudents;

select * from tblScores;

select * from tblFeedback;

-- select data using join statement
SELECT
  s.fname,
  s.lname,
  sc.score
FROM
  tblStudents as s
JOIN
  tblScores as sc
ON
  s.student_id = sc.student_id
WHERE
  s.fname = 'joe'
  AND s.lname = 'smith';
  
-- see all scores from join using in operator
SELECT
  s.fname,
  s.lname,
  sc.score
FROM
  tblStudents as s
JOIN
  tblScores as sc
ON
  s.student_id = sc.student_id
WHERE
  s.student_id in (1, 2, 3, 4); 
  