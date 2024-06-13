# inheritance part 1

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        return f"{self.name} is working."


# inheritance.
# Programmer merupakan turunan dari Employee
# Programmer akan mewarisi attribute dan method dari Employee
class Programmer(Employee):
    pass


employee = Employee("Rizqi", "rizqi@nintendo.com")
print(employee.work())

programmer = Programmer("Budi", "budi@nintendo.com")
print(programmer.work())


# extend.
# Programmer merupakan turunan dari Employee
# Programmer akan mewarisi attribute dan method dari Employee
# Programmer juga bisa mempunyai attribute dan method sendiri
class Programmer(Employee):
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level

    def debug(self):
        return f"{self.name} is debugging."


programmer = Programmer("Bayu", "bayu@nintendo.com", "senior")
print(programmer.work())
print(programmer.debug())
