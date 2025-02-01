class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name}, Age:{self.age}")

class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age) 
        self.employee_id=employee_id

    def display_employee_info(self):
        self.display()
        print(f"Employee ID:{self.employee_id}")

class Manager(Employee):
    def __init__(self,name,age,employee_id,department):
        super().__init__(name,age,employee_id) 
        self.department=department

    def approve_leave(self,leave_days):
        print(f"Leave for {leave_days} days has been approved.")

    def display_manager_info(self):
        self.display_employee_info()
        print(f"Department:{self.department}")

name=input("Enter name:")
age=int(input("Enter age:"))
employee_id=input("Enter employee ID:")
department=input("Enter department:")

person=Person(name,age)
employee=Employee(name,age,employee_id)
manager=Manager(name,age,employee_id,department)

print("\n")
print("Person Info:")
person.display()

print("\n")
print("Employee Info:")
employee.display_employee_info()

print("\n")
print("Manager Info:")
manager.display_manager_info()

print("\n")
leave_days = int(input("Enter leave days to approve:"))
manager.approve_leave(leave_days)
