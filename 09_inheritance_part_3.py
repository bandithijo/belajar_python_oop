# inheritance part 3

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        return f"{self.name} is working."


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


# polymorphism
def working(system):
    print(system.work())


# class yang bukan merupakan turunan dari Employee tapi memiliki method .work()
# seperti class yang merupakan turunan dari class Employee
class Manager:
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} is managing."


employee = Employee("Rizqi", "rizqi@nintendo.com")
print(employee.work())

programmer = Programmer("Bayu", "bayu@nintendo.com", "senior")
print(programmer.work())
print(programmer.debug())

ui_designer = UiDesigner("Bima", "bima@nintendo.com", "senior", "Figma")
print(ui_designer.work())

manager = Manager("Budi")
print(manager.work())

working(employee)
working(programmer)
working(ui_designer)
working(manager)
