#Command to Find Reviews Per School:

SELECT s.school_name, COUNT(r.id) AS num_reviews
FROM schools s
LEFT JOIN reviews r
  ON s.id = r.school_id
GROUP BY s.id, s.school_name
ORDER BY num_reviews DESC;


#Command to find Count of fully populated schools
SELECT COUNT(*) AS num_schools_with_15_reviews
FROM (
  SELECT s.id
  FROM schools s
  JOIN reviews r
    ON s.id = r.school_id
  GROUP BY s.id
  HAVING COUNT(r.id) = 15
) 