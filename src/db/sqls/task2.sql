SELECT
  departments.id,
  departments.department,
  COUNT(hired_employees.id) AS num_hires
FROM hired_employees
JOIN departments ON hired_employees.department_id = departments.id
WHERE strftime('%Y', hired_employees.datetime) = '2021'
GROUP BY departments.id, departments.department
HAVING num_hires > (SELECT AVG(num_hires) FROM (SELECT departments.id, COUNT(hired_employees.id) AS num_hires FROM hired_employees JOIN departments ON hired_employees.department_id = departments.id WHERE strftime('%Y', hired_employees.datetime) = '2021' GROUP BY departments.id) AS dept_hires_avg)
ORDER BY num_hires DESC