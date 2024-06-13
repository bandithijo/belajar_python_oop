# property

class User:
    total = 0  # class variable

    def __init__(self, name, email, role):
        self.name = name    # instance variable
        self.email = email  # instance variable
        self.__role = role  # private instance variable
        User.total += 1     # asignment ke class variable

    def info(self):
        return f"{self.name} - {self.email} - {self.__role}"

    def update_role(self, new_role):
        if self.__role != "User":
            self.__role = new_role

    def get_role(self):
        return self.__role

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role):
        if self.__role != "User":
            self.__role = new_role


# instansiasi object atau proses membuat object dari class User
zelda = User("Zelda", "zelda@nintendo.com", "Admin")
link = User("Link", "link@nintendo.com", "User")
mario = User("Mario", "mario@nintendo.com", "User")

print(zelda)
print(zelda.__dict__)
print(zelda.name)
print(zelda.email)
# print(zelda.role)
print(zelda.info())  # instance method

print(link)
print(link.__dict__)
print(link.name)
print(link.email)
# print(link.role)
print(link.info())  # instance method

print(mario)
print(mario.__dict__)
print(mario.name)
print(mario.email)
# print(mario.role)
print(mario.info())  # instance method

print(User.total)


# instance method untuk mengupdate role
print(zelda.info())
zelda.update_role("User")
print(zelda.info())
# zelda.update_role("Moderator")  # tidak bisa tembus
# zelda.__role = "Moderator"  # tidak bisa ditembus
print(zelda.__dict__)
zelda._User__role = "Moderator"  # bisa ditembus
print(zelda.__dict__)
print(zelda.info())
print(zelda._User__role)  # tidak elegant
print(zelda.get_role())  # kurang elegant

# pemanggilan dengan menggunakan decorator @property
zelda.role = "User"
print(zelda.role)
print(zelda.info())
zelda.role = "Moderator"
print(zelda.role)  # akan tetap memiliki role User
print(zelda.info())
