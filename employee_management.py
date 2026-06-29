"""
Employee Management System - File Based CRUD
Data stored directly in JSON file, no database needed
"""

import json
import os
from datetime import datetime

class EmployeeManagementSystem:
    def __init__(self):
        """Initialize the system with file-based storage"""
        self.filename = "employees.json"
        self.employees = []
        self.load_data()
    
    def load_data(self):
        """Load employee data from JSON file"""
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                with open(self.filename, 'r') as file:
                    self.employees = json.load(file)
                print(f"✅ Loaded {len(self.employees)} employee records from file")
            else:
                print("📝 No existing data found. Creating new file...")
                self.employees = []
                self.save_data()
        except json.JSONDecodeError:
            print("⚠️ File corrupted! Creating new file...")
            self.employees = []
            self.save_data()
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            self.employees = []
    
    def save_data(self):
        """Save employee data to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.employees, file, indent=4)
            return True
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return False
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("👔 EMPLOYEE MANAGEMENT SYSTEM")
        print("📁 FILE BASED CRUD OPERATIONS")
        print("="*50)
        print("1. ➕ CREATE - Add Employee")
        print("2. 📋 READ - View All Employees")
        print("3. 🔍 READ - Search Employee")
        print("4. ✏️ UPDATE - Update Employee")
        print("5. 🗑️ DELETE - Delete Employee")
        print("6. 💾 Save & Exit")
        print("="*50)
    
    # ============== CREATE OPERATION ==============
    def add_employee(self):
        """Add a new employee (CREATE)"""
        print("\n➡️ CREATE NEW EMPLOYEE")
        print("-" * 30)
        
        try:
            # Generate auto ID
            emp_id = self.generate_id()
            
            name = input("Enter Employee Name: ").strip()
            if not name:
                print("❌ Name is required!")
                return
            
            age = input("Enter Employee Age: ").strip()
            if not age or not age.isdigit():
                print("❌ Valid age is required!")
                return
            
            department = input("Enter Department: ").strip()
            if not department:
                print("❌ Department is required!")
                return
            
            salary = input("Enter Salary: ").strip()
            if not salary:
                print("❌ Salary is required!")
                return
            
            # Create employee dictionary
            employee = {
                'id': emp_id,
                'name': name,
                'age': int(age),
                'department': department,
                'salary': float(salary),
                'joining_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'status': 'Active'
            }
            
            # Add to list
            self.employees.append(employee)
            
            # Save to file immediately
            if self.save_data():
                print(f"✅ Employee '{name}' added successfully!")
                print(f"📝 Employee ID: {emp_id}")
            else:
                print("❌ Failed to save employee!")
            
        except ValueError:
            print("❌ Invalid input! Age and Salary must be numbers.")
        except Exception as e:
            print(f"❌ Error adding employee: {e}")
    
    def generate_id(self):
        """Generate unique employee ID"""
        if not self.employees:
            return "EMP001"
        else:
            # Get max ID and increment
            max_id = 0
            for emp in self.employees:
                emp_num = int(emp['id'].replace('EMP', ''))
                if emp_num > max_id:
                    max_id = emp_num
            return f"EMP{str(max_id + 1).zfill(3)}"
    
    # ============== READ OPERATION ==============
    def view_employees(self):
        """Display all employees (READ)"""
        print("\n📋 EMPLOYEE LIST - READ OPERATION")
        print("-" * 90)
        
        if not self.employees:
            print("📭 No employees found in file!")
            return
        
        # Headers
        print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Department':<15} {'Salary':<12} {'Status':<10} {'Joining Date'}")
        print("-" * 90)
        
        # Display each employee
        for emp in self.employees:
            print(f"{emp['id']:<10} {emp['name']:<20} {emp['age']:<5} {emp['department']:<15} ${emp['salary']:<11,.2f} {emp.get('status', 'Active'):<10} {emp.get('joining_date', 'N/A')}")
        
        print("-" * 90)
        print(f"📊 Total Employees: {len(self.employees)}")
        
        # Show statistics
        self.show_statistics()
    
    def show_statistics(self):
        """Show employee statistics"""
        if not self.employees:
            return
        
        print("\n📊 STATISTICS")
        print("-" * 40)
        
        # Department-wise count
        dept_count = {}
        total_salary = 0
        active_count = 0
        
        for emp in self.employees:
            dept = emp['department']
            dept_count[dept] = dept_count.get(dept, 0) + 1
            total_salary += emp['salary']
            if emp.get('status', 'Active') == 'Active':
                active_count += 1
        
        print("Department-wise Distribution:")
        for dept, count in dept_count.items():
            print(f"  {dept}: {count} employee(s)")
        
        print(f"\n📈 Total Employees: {len(self.employees)}")
        print(f"✅ Active Employees: {active_count}")
        print(f"💰 Total Salary: ${total_salary:,.2f}")
        print(f"💰 Average Salary: ${total_salary / len(self.employees):,.2f}")
    
    def search_employee(self):
        """Search for an employee (READ - Specific)"""
        print("\n🔍 SEARCH EMPLOYEE - READ OPERATION")
        print("-" * 30)
        
        search_term = input("Enter Employee ID or Name to search: ").strip()
        
        if not search_term:
            print("❌ Please enter search term!")
            return
        
        found = []
        
        # Search by ID or Name (partial match)
        for emp in self.employees:
            if (search_term.lower() in emp['id'].lower() or 
                search_term.lower() in emp['name'].lower()):
                found.append(emp)
        
        if found:
            print(f"\n✅ Found {len(found)} employee(s):")
            print("-" * 60)
            for emp in found:
                print(f"ID: {emp['id']}")
                print(f"Name: {emp['name']}")
                print(f"Age: {emp['age']}")
                print(f"Department: {emp['department']}")
                print(f"Salary: ${emp['salary']:,.2f}")
                print(f"Status: {emp.get('status', 'Active')}")
                print(f"Joining: {emp.get('joining_date', 'N/A')}")
                print("-" * 60)
        else:
            print(f"❌ No employee found with '{search_term}'!")
    
    # ============== UPDATE OPERATION ==============
    def update_employee(self):
        """Update an existing employee (UPDATE)"""
        print("\n✏️ UPDATE EMPLOYEE - UPDATE OPERATION")
        print("-" * 30)
        
        emp_id = input("Enter Employee ID to update: ").strip()
        
        if not emp_id:
            print("❌ Employee ID is required!")
            return
        
        # Find employee
        for i, emp in enumerate(self.employees):
            if emp['id'] == emp_id:
                print(f"\n📝 Updating details for: {emp['name']}")
                print("-" * 30)
                
                # Display current details
                print(f"Current Name: {emp['name']}")
                print(f"Current Age: {emp['age']}")
                print(f"Current Department: {emp['department']}")
                print(f"Current Salary: ${emp['salary']:,.2f}")
                print(f"Current Status: {emp.get('status', 'Active')}")
                print("-" * 30)
                
                try:
                    # Get new details
                    new_name = input("Enter new Name (press Enter to keep): ").strip()
                    if new_name:
                        emp['name'] = new_name
                    
                    new_age = input("Enter new Age (press Enter to keep): ").strip()
                    if new_age:
                        if new_age.isdigit():
                            emp['age'] = int(new_age)
                        else:
                            print("❌ Age must be a number! Keeping old value.")
                    
                    new_dept = input("Enter new Department (press Enter to keep): ").strip()
                    if new_dept:
                        emp['department'] = new_dept
                    
                    new_salary = input("Enter new Salary (press Enter to keep): ").strip()
                    if new_salary:
                        try:
                            emp['salary'] = float(new_salary)
                        except ValueError:
                            print("❌ Salary must be a number! Keeping old value.")
                    
                    new_status = input("Enter new Status (Active/Inactive) (press Enter to keep): ").strip()
                    if new_status:
                        emp['status'] = new_status
                    
                    emp['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Save to file
                    if self.save_data():
                        print("✅ Employee updated successfully!")
                    else:
                        print("❌ Failed to save updates!")
                    return
                    
                except Exception as e:
                    print(f"❌ Error updating employee: {e}")
                    return
        
        print(f"❌ Employee with ID '{emp_id}' not found!")
    
    # ============== DELETE OPERATION ==============
    def delete_employee(self):
        """Delete an employee (DELETE)"""
        print("\n🗑️ DELETE EMPLOYEE - DELETE OPERATION")
        print("-" * 30)
        
        emp_id = input("Enter Employee ID to delete: ").strip()
        
        if not emp_id:
            print("❌ Employee ID is required!")
            return
        
        # Find employee
        for i, emp in enumerate(self.employees):
            if emp['id'] == emp_id:
                print(f"\n⚠️ You are about to delete: {emp['name']}")
                print(f"Department: {emp['department']}")
                print(f"Salary: ${emp['salary']:,.2f}")
                
                confirm = input("\nAre you sure you want to delete? (yes/no): ").strip().lower()
                
                if confirm in ['yes', 'y']:
                    # Remove from list
                    deleted_emp = self.employees.pop(i)
                    
                    # Save to file
                    if self.save_data():
                        print(f"✅ Employee '{deleted_emp['name']}' (ID: {deleted_emp['id']}) deleted successfully!")
                    else:
                        print("❌ Failed to delete employee!")
                    return
                else:
                    print("❌ Deletion cancelled!")
                    return
        
        print(f"❌ Employee with ID '{emp_id}' not found!")
    
    # ============== FILE OPERATIONS ==============
    def backup_data(self):
        """Create backup of data file"""
        try:
            if os.path.exists(self.filename):
                backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(self.filename, 'r') as source:
                    with open(backup_name, 'w') as dest:
                        dest.write(source.read())
                print(f"✅ Backup created: {backup_name}")
                return True
        except Exception as e:
            print(f"❌ Backup failed: {e}")
            return False
    
    def view_file_info(self):
        """Show file information"""
        print("\n📁 FILE INFORMATION")
        print("-" * 30)
        
        if os.path.exists(self.filename):
            size = os.path.getsize(self.filename)
            print(f"File Name: {self.filename}")
            print(f"File Size: {size} bytes ({size/1024:.2f} KB)")
            print(f"Records: {len(self.employees)}")
            print(f"Last Modified: {datetime.fromtimestamp(os.path.getmtime(self.filename)).strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("❌ Data file not found!")
    
    # ============== MAIN LOOP ==============
    def run(self):
        """Main application loop"""
        print("\n" + "="*50)
        print("🚀 WELCOME TO EMPLOYEE MANAGEMENT SYSTEM")
        print("📁 FILE BASED CRUD OPERATIONS")
        print("="*50)
        print(f"📂 Data File: {self.filename}")
        print(f"📊 Current Records: {len(self.employees)}")
        print("="*50)
        
        while True:
            try:
                self.display_menu()
                choice = input("\n👉 Enter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.add_employee()  # CREATE
                elif choice == '2':
                    self.view_employees()  # READ - All
                elif choice == '3':
                    self.search_employee()  # READ - Specific
                elif choice == '4':
                    self.update_employee()  # UPDATE
                elif choice == '5':
                    self.delete_employee()  # DELETE
                elif choice == '6':
                    if self.save_data():
                        print("\n💾 Data saved successfully!")
                        print("👋 Thank you for using Employee Management System!")
                        print(f"📁 Data stored in: {self.filename}")
                        break
                elif choice == '7':
                    # Hidden admin options
                    self.admin_menu()
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
    
    def admin_menu(self):
        """Hidden admin menu for advanced operations"""
        print("\n🔧 ADMIN MENU")
        print("-" * 30)
        print("1. View File Info")
        print("2. Create Backup")
        print("3. Add Sample Data")
        print("4. Clear All Data")
        print("5. Back to Main Menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            self.view_file_info()
        elif choice == '2':
            self.backup_data()
        elif choice == '3':
            self.add_sample_data()
        elif choice == '4':
            self.clear_all_data()
        elif choice == '5':
            return
        else:
            print("❌ Invalid choice!")
    
    def add_sample_data(self):
        """Add sample employees for testing"""
        sample_employees = [
            {"id": "EMP001", "name": "Rahul Sharma", "age": 30, "department": "IT", "salary": 75000, "status": "Active"},
            {"id": "EMP002", "name": "Priya Patel", "age": 28, "department": "HR", "salary": 65000, "status": "Active"},
            {"id": "EMP003", "name": "Amit Kumar", "age": 35, "department": "Finance", "salary": 85000, "status": "Active"},
            {"id": "EMP004", "name": "Sneha Reddy", "age": 32, "department": "IT", "salary": 72000, "status": "Active"},
            {"id": "EMP005", "name": "Vikram Singh", "age": 40, "department": "Finance", "salary": 95000, "status": "Active"},
            {"id": "EMP006", "name": "Neha Gupta", "age": 26, "department": "Marketing", "salary": 58000, "status": "Active"},
            {"id": "EMP007", "name": "Rajesh Mishra", "age": 38, "department": "IT", "salary": 82000, "status": "Inactive"},
            {"id": "EMP008", "name": "Anjali Verma", "age": 29, "department": "HR", "salary": 68000, "status": "Active"}
        ]
        
        # Check for duplicates
        existing_ids = [emp['id'] for emp in self.employees]
        new_count = 0
        
        for emp in sample_employees:
            if emp['id'] not in existing_ids:
                emp['joining_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.employees.append(emp)
                new_count += 1
        
        if new_count > 0:
            self.save_data()
            print(f"✅ Added {new_count} sample employees!")
        else:
            print("📝 Sample data already exists!")
    
    def clear_all_data(self):
        """Clear all employee data"""
        confirm = input("⚠️ Are you sure you want to delete ALL data? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            self.employees = []
            self.save_data()
            print("✅ All data cleared!")
        else:
            print("❌ Operation cancelled!")

def main():
    """Main entry point"""
    try:
        system = EmployeeManagementSystem()
        system.run()
    except Exception as e:
        print(f"❌ Failed to start application: {e}")

if __name__ == "__main__":
    main()
