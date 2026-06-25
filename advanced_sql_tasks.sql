-- 1. Add Some Records:

INSERT INTO Employee VALUES
(111,'Aniket',88000,'2025-06-15',2),
(112,'Sakshi',72000,'2025-05-20',1),
(113,'Akash',68000,'2025-04-12',3);

-- 2. Apply Window Function:
RANK()
SELECT
emp_id,
emp_name,
salary,
RANK() OVER(ORDER BY salary DESC) AS Salary_Rank
FROM Employee;
ROW_NUMBER()
SELECT
emp_id,
emp_name,
salary,
ROW_NUMBER() OVER(ORDER BY salary DESC) AS Row_Num
FROM Employee;


-- 3. Apply View:
Create View
CREATE VIEW Employee_View AS
SELECT
e.emp_id,
e.emp_name,
e.salary,
d.dept_name
FROM Employee e
INNER JOIN Department d
ON e.dept_id=d.dept_id;
Display View
SELECT * FROM Employee_View;


-- 4. Apply Trigger:
Log Table
CREATE TABLE Employee_Log(
log_id INT AUTO_INCREMENT PRIMARY KEY,
emp_id INT,
action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Trigger
DELIMITER $$

CREATE TRIGGER trg_employee_insert
AFTER INSERT ON Employee
FOR EACH ROW
BEGIN
INSERT INTO Employee_Log(emp_id)
VALUES(NEW.emp_id);
END$$

DELIMITER ;
Test Trigger
INSERT INTO Employee
VALUES(114,'Rohan',65000,'2025-06-20',4);
Check Log
SELECT * FROM Employee_Log;


-- 5. Handle CASE WHEN:
SELECT
emp_name,
salary,
CASE
WHEN salary >= 90000 THEN 'High Salary'
WHEN salary >= 70000 THEN 'Medium Salary'
ELSE 'Low Salary'
END AS Salary_Category
FROM Employee;
