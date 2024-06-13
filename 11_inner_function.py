# 11 inner function

"""
inner function adalah method yang berada di dalam method.
"""


class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def info(self):
        def print_title():
            return f"Title: {self.title}"

        def print_price():
            return f"Price: {self.price}"

        return print_title, print_price


zelda = Game("Breath of The Wild", 89)
title, price = zelda.info()
print(title())
print(price())
