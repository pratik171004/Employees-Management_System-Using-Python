import mysql.connector
from tabulate import tabulate

# Database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pratik@16",
    database="emp"
)

cursor = con.cursor()

# Function to add employee
def add_employee(name, position, salary, department, status="Active"):
    query = "INSERT INTO employees (name, position, salary, department, status) VALUES (%s, %s, %s, %s, %s)"
    values = (name, position, salary, department, status)
    cursor.execute(query, values)
    con.commit()
    print("✅ Employee added successfully!")

# Function to remove employee by ID
def remove_employee(emp_id):
    cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
    if cursor.fetchone() is None:
        print("❌ Employee not found!")
        return
    query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(query, (emp_id,))
    con.commit()
    print("✅ Employee removed successfully!")

# Function to promote employee (update position/salary)
def promote_employee(emp_id, new_position, new_salary):
    cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
    if cursor.fetchone() is None:
        print("❌ Employee not found!")
        return
    query = "UPDATE employees SET position = %s, salary = %s WHERE id = %s"
    values = (new_position, new_salary, emp_id)
    cursor.execute(query, values)
    con.commit()
    print("✅ Employee promoted successfully!")

# Function to update employee details
def update_employee(emp_id, field, new_value):
    if field not in ["name", "position", "salary", "department", "status"]:
        print("❌ Invalid field!")
        return
    query = f"UPDATE employees SET {field} = %s WHERE id = %s"
    cursor.execute(query, (new_value, emp_id))
    con.commit()
    print("✅ Employee updated successfully!")

# Function to search employee by ID
def search_employee_by_id(emp_id):
    cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
    row = cursor.fetchone()
    if row:
        print(tabulate([row], headers=["ID", "Name", "Position", "Salary", "Department", "Hire Date", "Status"], tablefmt="grid"))
    else:
        print("❌ Employee not found!")

# Function to search employee by name
def search_employee_by_name(name):
    cursor.execute("SELECT * FROM employees WHERE name LIKE %s", ('%' + name + '%',))
    rows = cursor.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Position", "Salary", "Department", "Hire Date", "Status"], tablefmt="grid"))
    else:
        print("❌ No employees found with that name!")

# Function to display employees
def display_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Position", "Salary", "Department", "Hire Date", "Status"], tablefmt="grid"))
    else:
        print("⚠️ No employees in the system.")

# Function to filter employees by department
def filter_by_department(dept):
    cursor.execute("SELECT * FROM employees WHERE department = %s", (dept,))
    rows = cursor.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Position", "Salary", "Department", "Hire Date", "Status"], tablefmt="grid"))
    else:
        print(f"⚠️ No employees found in department '{dept}'.")

# Function to filter employees by status
def filter_by_status(status):
    cursor.execute("SELECT * FROM employees WHERE status = %s", (status,))
    rows = cursor.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Position", "Salary", "Department", "Hire Date", "Status"], tablefmt="grid"))
    else:
        print(f"⚠️ No employees found with status '{status}'.")

# Menu-driven system
def menu():
    while True:
        print("\n=== Employee Management System ===")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Promote Employee")
        print("4. Update Employee Details")
        print("5. Search Employee by ID")
        print("6. Search Employee by Name")
        print("7. Display All Employees")
        print("8. Filter Employees by Department")
        print("9. Filter Employees by Status")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter employee name: ")
            position = input("Enter position: ")
            try:
                salary = float(input("Enter salary: "))
            except ValueError:
                print("❌ Invalid salary input!")
                continue
            department = input("Enter department: ")
            status = input("Enter status (Active/Resigned/Terminated) [default Active]: ") or "Active"
            add_employee(name, position, salary, department, status)

        elif choice == 2:
            emp_id = int(input("Enter employee ID to remove: "))
            remove_employee(emp_id)

        elif choice == 3:
            emp_id = int(input("Enter employee ID to promote: "))
            new_position = input("Enter new position: ")
            try:
                new_salary = float(input("Enter new salary: "))
            except ValueError:
                print("❌ Invalid salary input!")
                continue
            promote_employee(emp_id, new_position, new_salary)

        elif choice == 4:
            emp_id = int(input("Enter employee ID to update: "))
            field = input("Enter field to update (name/position/salary/department/status): ").lower()
            new_value = input("Enter new value: ")
            if field == "salary":
                try:
                    new_value = float(new_value)
                except ValueError:
                    print("❌ Invalid salary input!")
                    continue
            update_employee(emp_id, field, new_value)

        elif choice == 5:
            emp_id = int(input("Enter employee ID to search: "))
            search_employee_by_id(emp_id)

        elif choice == 6:
            name = input("Enter employee name to search: ")
            search_employee_by_name(name)

        elif choice == 7:
            display_employees()

        elif choice == 8:
            dept = input("Enter department to filter: ")
            filter_by_department(dept)

        elif choice == 9:
            status = input("Enter status to filter (Active/Resigned/Terminated): ")
            filter_by_status(status)

        elif choice == 10:
            print("👋 Exiting program... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

# Run the program
menu()

# Close connection
cursor.close()
con.close()
