# inheritance part 2

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


# override.
# Programmer merupakan turunan dari Employee
# Programmer akan mewarisi attribute dan method dari Employee
# Programmer juga bisa mempunyai attribute dan method sendiri
# Programmer juga dapat mengoverride method yang dimiliki parent
class Programmer(Employee):
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level

    def debug(self):
        return f"{self.name} is debugging."

    def work(self):
        return f"{self.name} is writing code."


class UiDesigner(Employee):
    def __init__(self, name, email, level, tools):
        super().__init__(name, email)
        self.tools = tools

    def work(self):
        return f"{self.name} is designing using {self.tools}."


programmer = Programmer("Bayu", "bayu@nintendo.com", "senior")
print(programmer.work())
print(programmer.debug())

ui_designer = UiDesigner("Bima", "bima@nintendo.com", "senior", "Figma")
print(ui_designer.work())
