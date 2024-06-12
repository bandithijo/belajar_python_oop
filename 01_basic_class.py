# basic class

class User:
    pass


# instansiasi object yang tidak baik
zelda = User()
link = User()

# pendefinisian attribute name yang tidak baik
zelda.name = "Zelda"
link.name = "Link"

print(zelda)
print(zelda.__dict__)
print(zelda.name)
print(link)
print(link.__dict__)
print(link.name)
