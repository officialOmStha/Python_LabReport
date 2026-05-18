# Lab 3:

# Base class
class Employee:

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.id = emp_id
        self.salary = salary

    # Method to display employee information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")


# Derived class: Manager
class Manager(Employee):

    def __init__(self, name, emp_id, salary, bonus):
        super().__init__(name, emp_id, salary)
        self.bonus = bonus

    # Overriding display_info()
    def display_info(self):
        print("\n--- Manager Information ---")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")
        print(f"Bonus: {self.bonus}")


# Derived class: Developer
class Developer(Employee):

    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    # Overriding display_info()
    def display_info(self):
        print("\n--- Developer Information ---")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")
        print(f"Programming Language: {self.programming_language}")


# Main program

# Creating objects
emp1 = Manager("Ram", 101, 70000, 15000)
emp2 = Developer("Sita", 102, 60000, "Python")
emp3 = Developer("Hari", 103, 55000, "Java")

# List of employees
employees = [emp1, emp2, emp3]

# Polymorphism using loop
for emp in employees:

    # Calling overridden methods
    emp.display_info()

    # Using match-case
    match emp.__class__.__name__:

        case "Manager":
            print("This employee is a Manager.")

        case "Developer":
            print("This employee is a Developer.")

        case _:
            print("Unknown employee type.")