
-- 1. List the following details of each employee: employee number, 
-- last name, first name, sex, and salary.

SELECT employees.emp_no,
		employees.last_name,
		employees.first_name,
		employees.sex,
		salaries.salary
FROM employees
JOIN salaries ON salaries.emp_no = employees.emp_no;

--2. List first name, last name, and hire date for employees who 
-- were hired in 1986.

select first_name,
		last_name,
		hire_date
from employees 
WHERE hire_date >= '1986-01-01' 
AND hire_date <= '1986-12-31';

--3. List the manager of each department with the following information
--: department number, department name, the manager's employee number, last name, 
--first name.

SELECT dept_manager.dept_no,
		departments.dept_name,
		employees.emp_no,
		employees.last_name,
		employees.first_name
FROM employees
JOIN dept_manager on dept_manager.emp_no = employees.emp_no
JOIN departments on dept_manager.dept_no = departments.dept_no

--4. List the department of each employee with the following 
--information: employee number, last name, first name, and 
--department name.

select employees.emp_no,
		employees.last_name,
		employees.first_name,
		departments.dept_name
from employees
JOIN dept_emp on employees.emp_no = dept_emp.emp_no
JOIN departments on dept_emp.dept_no = departments.dept_no;

--5. List first name, last name, and sex for employees whose 
--first name is "Hercules" and last names begin with "B."

SELECT first_name,
		last_name,
		sex
FROM EMPLOYEES 
WHERE first_name = 'Hercules' 
and last_name LIKE 'B%';

--6. List all employees in the Sales department, including their 
--employee number, last name, first name, and department name.

select employees.emp_no,
		employees.last_name,
		employees.first_name,
		departments.dept_name
from employees
JOIN dept_emp on employees.emp_no = dept_emp.emp_no
JOIN departments on dept_emp.dept_no = departments.dept_no
WHERE dept_name = 'Sales';

--7. List all employees in the Sales and Development departments, 
--including their employee number, last name, first name, and department name.
select employees.emp_no,
		employees.last_name,
		employees.first_name,
		departments.dept_name
from employees
JOIN dept_emp on employees.emp_no = dept_emp.emp_no
JOIN departments on dept_emp.dept_no = departments.dept_no
WHERE dept_name = 'Sales' 
or dept_name = 'Development';

--8. In descending order, list the frequency count of employee 
--last names, i.e., how many employees share each last name.
select last_name
	,count(last_name) as "Last Name Count" 
	from employees
	GROUP BY last_name
	ORDER BY "Last Name Count" DESC;