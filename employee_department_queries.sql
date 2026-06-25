CREATE DATABASE internship_sql;
USE internship_sql;

-- Department Table
CREATE TABLE Departmentt(
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- Employee Table
CREATE TABLE Employee(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Insert Department Data
INSERT INTO Department VALUES
(1,'HR'),
(2,'IT'),
(3,'Finance'),
(4,'Marketing');

-- Insert Employee Data
INSERT INTO Employee VALUES
(101,'Amit',50000,'2025-02-10',1),
(102,'Rahul',70000,'2025-03-15',2),
(103,'Sneha',90000,'2025-04-20',2),
(104,'Pooja',65000,'2025-05-01',3),
(105,'Vikas',80000,'2025-01-18',2),
(106,'Neha',55000,'2025-06-01',4),
(107,'Rohit',95000,'2025-02-28',3),
(108,'Anjali',60000,'2025-05-15',1),
(109,'Karan',75000,'2025-04-10',4),
(110,'Priya',85000,'2025-03-05',2);

-- 1. Top 5 Highest Salary Employees
SELECT *
FROM Employee
ORDER BY salary DESC
LIMIT 5;

-- 2. Department Wise Employee Count
SELECT d.dept_name,
COUNT(e.emp_id) AS employee_count
FROM Department d
JOIN Employee e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

-- 3. Find Second Highest Salary
SELECT MAX(salary) AS second_highest_salary
FROM Employee
WHERE salary <
(
SELECT MAX(salary)
FROM Employee
);

-- 4. Employees Whose Salary > Department Average Salary
SELECT emp_name,salary,dept_id
FROM Employee e
WHERE salary >
(
SELECT AVG(salary)
FROM Employee
WHERE dept_id = e.dept_id
);

-- 5. Inner Join
SELECT e.emp_id,
e.emp_name,
d.dept_name
FROM Employee e
INNER JOIN Department d
ON e.dept_id = d.dept_id;

-- 6. Left Join
SELECT e.emp_id,
e.emp_name,
d.dept_name
FROM Employee e
LEFT JOIN Department d
ON e.dept_id = d.dept_id;

-- 7. Group By With Having
SELECT dept_id,
COUNT(*) AS total_employees
FROM Employee
GROUP BY dept_id
HAVING COUNT(*) > 2;

-- 8. Employees Hired In Last 6 Months
SELECT *
FROM Employee
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);

-- 9. Find Duplicate Records
SELECT emp_name,
COUNT(*) AS total
FROM Employee
GROUP BY emp_name
HAVING COUNT(*) > 1;

-- 10. Remove Duplicate Records
DELETE e1
FROM Employee e1
INNER JOIN Employee e2
ON e1.emp_name = e2.emp_name
AND e1.emp_id > e2.emp_id;