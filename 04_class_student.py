class Student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
        
    def display(self):
        print(f"Details:\n Name of the student:{self.name} \n Roll Number of the student:{self.rno}")

print("Enter the student's name:")
name=input()
print("Enter the student's roll number:")
rno=int(input())

student=Student(name,rno)
student.display()