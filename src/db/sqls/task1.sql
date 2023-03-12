SELECT
  departments.department,
  jobs.job,
  COUNT(CASE WHEN strftime('%Y', hired_employees.datetime) = '2021' AND strftime('%m', hired_employees.datetime) BETWEEN '01' AND '03' THEN 1 END) AS Q1,
  COUNT(CASE WHEN strftime('%Y', hired_employees.datetime) = '2021' AND strftime('%m', hired_employees.datetime) BETWEEN '04' AND '06' THEN 1 END) AS Q2,
  COUNT(CASE WHEN strftime('%Y', hired_employees.datetime) = '2021' AND strftime('%m', hired_employees.datetime) BETWEEN '07' AND '09' THEN 1 END) AS Q3,
  COUNT(CASE WHEN strftime('%Y', hired_employees.datetime) = '2021' AND strftime('%m', hired_employees.datetime) BETWEEN '10' AND '12' THEN 1 END) AS Q4
FROM hired_employees
JOIN departments ON hired_employees.department_id = departments.id
JOIN jobs ON hired_employees.job_id = jobs.id
WHERE strftime('%Y', hired_employees.datetime) = '2021'
GROUP BY departments.department, jobs.job
ORDER BY departments.department, jobs.job
