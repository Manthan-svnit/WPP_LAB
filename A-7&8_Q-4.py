class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        raise TypeError("Operand must be an instance of Employee")

    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary
        raise TypeError("Operand must be an instance of Employee")

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        raise TypeError("Operand must be an instance of Employee")

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        raise TypeError("Operand must be an instance of Employee")

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.salary == other.salary
        raise TypeError("Operand must be an instance of Employee")

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1 + emp2)  
print(emp1 - emp2) 
print(emp1 > emp2) 
print(emp1 < emp2) 
print(emp1 == emp2)