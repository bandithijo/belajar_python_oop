# magic method

"""
ciri-ciri magic method, dipanggil namun tidak perlu memanggil nama methodnya.
"""


class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} - USD${self.price}"

    def __eq__(self, other):
        return self.title == other.title

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, other):
        return self.price + other.price


zelda1 = Game("Breath of The Wild", 89)
zelda2 = Game("Breath of The Wild", 85)
mario = Game("Paper Mario Origami King", 57)

print(zelda1.title)

# __str__
print(zelda1)

# __eq__
print(zelda1 == mario)
print(zelda1 == zelda2)

# __gt__
print(zelda1 > mario)
print(mario > zelda1)
print(zelda1 > zelda2)
print(zelda2 > zelda1)

# __add__
print(zelda1 + mario)
print(zelda2 + mario)
print(zelda1 + zelda2)
