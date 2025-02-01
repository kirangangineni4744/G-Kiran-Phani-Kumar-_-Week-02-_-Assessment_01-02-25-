class Employee():
    def __init__(self,name,id,department):
        self.name=name 
        self.id=id 
        self.department=department

print("Enter the employee name:")
name=input()
print("Enter the employee ID:")
id=int(input())
print("Enter the department of the employee:")
department=input()

emp1=Employee(name,id,department)

print(f"The employee named {emp1.name}, of the id {emp1.id}, belongs to the {emp1.department} department")