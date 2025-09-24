class Employee:
    def __init__(self,id,name,age,department,designation,reportingto):
        self.id=id
        self.name=name
        self.age=age
        self.department=department
        self.designation=designation
        self.reportingto=reportingto
employee=[  Employee(1, "Alice", 30, "HR", "Manager", None),
            Employee(2, "Bob", 25, "HR", "Executive", "Alice"),
            Employee(3, "Charlie", 28, "IT", "Developer", "Eve"),
            Employee(4, "David", 32, "IT", "Lead", "Eve"),
            Employee(5, "Eve", 40, "IT", "Manager", "Alice"),
            Employee(6, "Frank", 35, "Finance", "Analyst", "Grace"),
            Employee(7, "Grace", 45, "Finance", "Manager", "Alice"),
            Employee(8, "Helen", 29, "Marketing", "Executive", "Ivy"),
            Employee(9, "Ivy", 38, "Marketing", "Manager", "Alice"),
            Employee(10, "Jack", 26, "IT", "Developer", "David"),]     