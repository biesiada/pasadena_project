-- Join 1:
-- This is a left join that returns all rows from the tblStudents table, 
-- and all rows from the -- tblScores table and the tblFeedback table 
-- where the student_id column in the tblStudents table is equal 
-- to the student_id column in the tblScores table and the tblFeedback table.
SELECT s.student_id, s.fname, s.lname, sc.score, f.feedback
FROM tblStudents s
LEFT JOIN tblScores sc ON s.student_id = sc.student_id
LEFT JOIN tblFeedback f ON s.student_id = f.student_id;

-- Join 2:
-- 
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
  
-- Join 3 
SELECT s.student_id, s.fname, s.lname, sc.score, f.feedback
FROM tblStudents s
LEFT JOIN tblScores sc ON s.student_id = sc.student_id
LEFT JOIN tblFeedback f ON s.student_id = f.student_id
WHERE f.feedback IS NOT NULL
ORDER BY s.fname, s.lname;






