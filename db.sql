-- Create database if it doesn’t already exist
CREATE DATABASE IF NOT EXISTS emp;

-- Switch to the database
USE emp;

-- Remove existing employees table if present (for fresh setup)
DROP TABLE IF EXISTS employees;

-- Create the employees table
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique employee ID (auto-generated)
    name VARCHAR(100) NOT NULL,                 -- Full name of the employee
    position VARCHAR(100) NOT NULL,             -- Job title (e.g., Software Engineer, HR Manager)
    salary DECIMAL(10,2) NOT NULL DEFAULT 0.00, -- Salary with 2 decimal precision, default = 0.00
    department VARCHAR(100) NOT NULL,           -- Department name (IT, HR, Sales, etc.)
    hire_date DATE NOT NULL,                    -- Date of hiring (auto-filled by trigger if not given)
    status ENUM('Active','Resigned','Terminated') NOT NULL DEFAULT 'Active'
                                                 -- Current status of employee
                                                 -- Allowed values: Active, Resigned, Terminated
);

-- Trigger: Automatically set hire_date to today if not provided during insert
DELIMITER //
CREATE TRIGGER employees_set_hire_date
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
  -- If no hire_date is provided, use current date
  IF NEW.hire_date IS NULL THEN
    SET NEW.hire_date = CURDATE();
  END IF;
END//
DELIMITER ;
