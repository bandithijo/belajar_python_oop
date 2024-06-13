# simple decorator part 1

"""
inner function adalah method yang berada di dalam method.
"""


def info(func):
    def wrapper():
        print("*" * 10)
        func()
        print("#" * 10)

    return wrapper


def say_hello():
    print("HELLO WORLD OF PYTHON")


say_hello()

print("")

get_hello = info(say_hello)
get_hello()
