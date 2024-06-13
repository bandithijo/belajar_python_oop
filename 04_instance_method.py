# instance method

class User:
    total = 0  # class variable

    def __init__(self, name, email, role):
        self.name = name    # instance variable
        self.email = email  # instance variable
        self.role = role    # instance variable
        User.total += 1     # asignment ke class variable

    def info(self):
        return f"{self.name} - {self.email} - {self.role}"

    def update_role(self, new_role):
        if self.role != "User":
            self.role = new_role


# instansiasi object atau proses membuat object dari class User
zelda = User("Zelda", "zelda@nintendo.com", "Admin")
link = User("Link", "link@nintendo.com", "User")
mario = User("Mario", "mario@nintendo.com", "User")

print(zelda)
print(zelda.__dict__)
print(zelda.name)
print(zelda.email)
print(zelda.role)
print(zelda.info())  # instance method

print(link)
print(link.__dict__)
print(link.name)
print(link.email)
print(link.role)
print(link.info())  # instance method

print(mario)
print(mario.__dict__)
print(mario.name)
print(mario.email)
print(mario.role)
print(mario.info())  # instance method

print(User.total)


# instance method untuk mengupdate role
print(zelda.info())
zelda.update_role("User")
print(zelda.info())
# zelda.update_role("Moderator")  # tidak bisa tembus
zelda.role = "Moderator"  # masih bisa ditembus
print(zelda.info())
