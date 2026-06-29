"""
Employee Management System
A comprehensive Python application for managing employee records
"""

import json
import os
from datetime import datetime

class EmployeeManagementSystem:
    def __init__(self):
        """Initialize the Employee Management System"""
        self.employees = []
        self.filename = "employees_data.json"
        self.load_data()
    
    def load_data(self):
        """Load employee data from JSON file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.employees = json.load(file)
                print(f"✅ Loaded {len(self.employees)} employee records")
            else:
                print("📝 No existing data found. Starting with empty database.")
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            self.employees = []
    
    def save_data(self):
        """Save employee data to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.employees, file, indent=4)
            print("💾 Data saved successfully!")
            return True
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return False
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("👔 EMPLOYEE MANAGEMENT SYSTEM")
        print("="*50)
        print("1. ➕ Add Employee")
        print("2. 📋 View All Employees")
        print("3. 🔍 Search Employee")
        print("4. ✏️ Update Employee")
        print("5. 🗑️ Delete Employee")
        print("6. 💾 Save & Exit")
        print("="*50)
    
    def add_employee(self):
        """Add a new employee"""
        print("\n➡️ ADD NEW EMPLOYEE")
        print("-" * 30)
        
        try:
            # Input employee details
            emp_id = input("Enter Employee ID: ").strip()
            
            # Check if ID already exists
            if any(emp['id'] == emp_id for emp in self.employees):
                print("❌ Employee ID already exists!")
                return
            
            name = input("Enter Employee Name: ").strip()
            age = input("Enter Employee Age: ").strip()
            department = input("Enter Department: ").strip()
            salary = input("Enter Salary: ").strip()
            
            # Validate inputs
            if not all([emp_id, name, age, department, salary]):
                print("❌ All fields are required!")
                return
            
            # Create employee dictionary
            employee = {
                'id': emp_id,
                'name': name,
                'age': int(age),
                'department': department,
                'salary': float(salary),
                'joining_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Add to list
            self.employees.append(employee)
            print(f"✅ Employee '{name}' added successfully!")
            
        except ValueError:
            print("❌ Invalid input! Age must be a number and Salary must be a number.")
        except Exception as e:
            print(f"❌ Error adding employee: {e}")
    
    def view_employees(self):
        """Display all employees in tabular format"""
        print("\n📋 EMPLOYEE LIST")
        print("-" * 80)
        
        if not self.employees:
            print("📭 No employees found!")
            return
        
        # Headers
        print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Department':<15} {'Salary':<12} {'Joining Date'}")
        print("-" * 80)
        
        # Display each employee
        for emp in self.employees:
            print(f"{emp['id']:<10} {emp['name']:<20} {emp['age']:<5} {emp['department']:<15} ${emp['salary']:<11,.2f} {emp.get('joining_date', 'N/A')}")
        
        print("-" * 80)
        print(f"📊 Total Employees: {len(self.employees)}")
    
    def search_employee(self):
        """Search for an employee by ID"""
        print("\n🔍 SEARCH EMPLOYEE")
        print("-" * 30)
        
        emp_id = input("Enter Employee ID to search: ").strip()
        
        for emp in self.employees:
            if emp['id'] == emp_id:
                print("\n✅ Employee Found!")
                print("-" * 40)
                print(f"ID          : {emp['id']}")
                print(f"Name        : {emp['name']}")
                print(f"Age         : {emp['age']}")
                print(f"Department  : {emp['department']}")
                print(f"Salary      : ${emp['salary']:,.2f}")
                print(f"Joining Date: {emp.get('joining_date', 'N/A')}")
                print("-" * 40)
                return
        
        print(f"❌ Employee with ID '{emp_id}' not found!")
    
    def update_employee(self):
        """Update an existing employee's details"""
        print("\n✏️ UPDATE EMPLOYEE")
        print("-" * 30)
        
        emp_id = input("Enter Employee ID to update: ").strip()
        
        # Find employee
        for emp in self.employees:
            if emp['id'] == emp_id:
                print(f"\n📝 Updating details for: {emp['name']}")
                print("-" * 30)
                
                # Display current details
                print(f"Current Name: {emp['name']}")
                print(f"Current Age: {emp['age']}")
                print(f"Current Department: {emp['department']}")
                print(f"Current Salary: ${emp['salary']:,.2f}")
                print("-" * 30)
                
                try:
                    # Get new details
                    new_name = input("Enter new Name (press Enter to keep current): ").strip()
                    if new_name:
                        emp['name'] = new_name
                    
                    new_age = input("Enter new Age (press Enter to keep current): ").strip()
                    if new_age:
                        emp['age'] = int(new_age)
                    
                    new_dept = input("Enter new Department (press Enter to keep current): ").strip()
                    if new_dept:
                        emp['department'] = new_dept
                    
                    new_salary = input("Enter new Salary (press Enter to keep current): ").strip()
                    if new_salary:
                        emp['salary'] = float(new_salary)
                    
                    emp['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print("✅ Employee updated successfully!")
                    return
                    
                except ValueError:
                    print("❌ Invalid input! Age and Salary must be numbers.")
                    return
        
        print(f"❌ Employee with ID '{emp_id}' not found!")
    
    def delete_employee(self):
        """Delete an employee by ID"""
        print("\n🗑️ DELETE EMPLOYEE")
        print("-" * 30)
        
        emp_id = input("Enter Employee ID to delete: ").strip()
        
        # Find and remove employee
        for i, emp in enumerate(self.employees):
            if emp['id'] == emp_id:
                print(f"\n⚠️ You are about to delete: {emp['name']}")
                confirm = input("Are you sure? (yes/no): ").strip().lower()
                
                if confirm in ['yes', 'y']:
                    deleted_emp = self.employees.pop(i)
                    print(f"✅ Employee '{deleted_emp['name']}' deleted successfully!")
                    return
                else:
                    print("❌ Deletion cancelled!")
                    return
        
        print(f"❌ Employee with ID '{emp_id}' not found!")
    
    def get_statistics(self):
        """Display employee statistics"""
        if not self.employees:
            return
        
        print("\n📊 EMPLOYEE STATISTICS")
        print("-" * 40)
        
        # Department-wise count
        dept_count = {}
        total_salary = 0
        
        for emp in self.employees:
            dept = emp['department']
            dept_count[dept] = dept_count.get(dept, 0) + 1
            total_salary += emp['salary']
        
        print("Department-wise Distribution:")
        for dept, count in dept_count.items():
            print(f"  {dept}: {count} employee(s)")
        
        print(f"\n💰 Average Salary: ${total_salary / len(self.employees):,.2f}")
        print(f"💰 Total Salary: ${total_salary:,.2f}")
    
    def run(self):
        """Main application loop"""
        print("\n🚀 Welcome to Employee Management System!")
        
        while True:
            try:
                self.display_menu()
                choice = input("\n👉 Enter your choice (1-6): ").strip()
                
                if choice == '1':
                    self.add_employee()
                elif choice == '2':
                    self.view_employees()
                    self.get_statistics()
                elif choice == '3':
                    self.search_employee()
                elif choice == '4':
                    self.update_employee()
                elif choice == '5':
                    self.delete_employee()
                elif choice == '6':
                    if self.save_data():
                        print("\n👋 Thank you for using Employee Management System!")
                        break
                elif choice == '7':
                    # Hidden option for advanced features
                    self.advanced_demo()
                else:
                    print("❌ Invalid choice! Please select 1-6.")
                
                # Pause for user to see output
                if choice != '6':
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n⚠️ Interrupted! Saving data...")
                self.save_data()
                break
            except Exception as e:
                print(f"❌ An unexpected error occurred: {e}")
                input("Press Enter to continue...")
    
    def advanced_demo(self):
        """Demo of advanced features (for testing)"""
        print("\n🔧 ADVANCED FEATURES DEMO")
        print("-" * 30)
        
        # Add sample data
        sample_employees = [
            {"id": "EMP001", "name": "John Doe", "age": 30, "department": "IT", "salary": 75000},
            {"id": "EMP002", "name": "Jane Smith", "age": 28, "department": "HR", "salary": 65000},
            {"id": "EMP003", "name": "Bob Johnson", "age": 35, "department": "Finance", "salary": 85000},
            {"id": "EMP004", "name": "Alice Brown", "age": 32, "department": "IT", "salary": 72000},
            {"id": "EMP005", "name": "Charlie Wilson", "age": 40, "department": "Finance", "salary": 95000}
        ]
        
        for emp in sample_employees:
            if not any(e['id'] == emp['id'] for e in self.employees):
                emp['joining_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.employees.append(emp)
        
        print("✅ Sample employees added successfully!")

def main():
    """Main entry point"""
    try:
        system = EmployeeManagementSystem()
        system.run()
    except Exception as e:
        print(f"❌ Failed to start application: {e}")

if __name__ == "__main__":
    main()
