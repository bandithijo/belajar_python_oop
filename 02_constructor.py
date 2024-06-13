# basic class

class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role


# instansiasi object atau proses membuat object dari class User
zelda = User("Zelda", "zelda@nintendo.com", "Admin")
link = User("Link", "link@nintendo.com", "User")

print(zelda)
print(zelda.__dict__)
print(zelda.name)
print(zelda.email)
print(zelda.role)

print(link)
print(link.__dict__)
print(link.name)
print(link.email)
print(link.role)
