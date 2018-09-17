#Patient Class
class Patient:
    def __init__(self, first, phone, last, ID, age, primary):
        self.first = first
        self.last = last
        self.phone = phone
        self.ID = ID
        self.age = age
        self.salary = primary

    def print_patient_detials(self):
        print(self.first, self.last, self.phone,  self.ID, self.age, self.salary)

#Student Class
class Student:
    def __init__(self, sID, school):
        self.sID = sID
        self.school = school
        self.grade = "ungraded"
        self.evaluation = "unevaluated"

    #private member
    def __give_grade(self, grade, eval):
        self.grade = grade
        self.evaluation = eval

    def evaluate(self, evaluation, grade):
        self.__give_grade(grade, evaluation)

    def print_student_details(self):
        print(self.sID, self.school, "EVALUATION: " + self.evaluation + ",", "GRADE: " + self.grade)

#Parent class for Employees of the hospital
class Employee:
    def __init__(self, first, last, ID, age, title, salary, department):
        self.first = first
        self.last = last
        self.ID = ID
        self.age = age
        self.title = title
        self.salary = salary
        self.department = department

    def print_details(self):
        print(self.first, self.last, self.ID, self.age, self.title, self.salary, self.department)

#Intern Class that is a child of both Employee and student
class Intern(Employee, Student):
    def __init__(self, first, last, ID, age, title, salary, department, sID, school):
        Employee.__init__(self, first, last, ID, age, title, salary, department)
        Student.__init__(self, sID, school)

#Physician class that is child of Employee and uses super()
class Physician(Employee):
    def __init__(self, first, last, ID, age, title, salary, department):
        super().__init__(first, last, ID, age, title, salary, department)

#Nurse class that is child of Employee
class Nurse(Employee):
    def __init__(self, first, last, ID, age, title, salary, department, nurseManager ):
        Employee.__init__(self, first, last, ID, age, title, salary, department)
        self.nurseManager = nurseManager


#Tests
print("Employee Class Test: Parent Class for employees of the hospital")
testEmp = Employee("John", "Smith", 111111, 11, "Employee", 1111111, "Department")
testEmp.print_details()

print("\n Physician Class Test: child of Employee")
testDR = Physician("Alex", "Larios", 12345, 25, "Doctor", 160000, "ER")
testDR.print_details()

print("\n Nurse Class Test: child of Employee")
testNurse = Nurse("Payton", "long", 2345, 24, "Nurse", 77000, "ER", "Manager: cindy")
testNurse.print_details()

print("\n Student Class Test: Parent of Intern")
testStudent = Student(987654321, "UMKC")
testStudent.print_student_details()

print("\n Intern Class Test: child of Employee and Student")
testIntern = Intern("Carly", "Dorms", 54321, 23, "Intern", 0, "Clinic", 1294234, "UMKC")
testIntern.evaluate("Student did well", "pass")
testIntern.print_details()
testIntern.print_student_details()