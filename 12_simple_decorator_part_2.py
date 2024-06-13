# simple decorator part 2

"""
inner function adalah method yang berada di dalam method.
"""


def info(func):
    def wrapper():
        print("*" * 10)
        func()
        print("#" * 10)

    return wrapper


@info
def say_hello():
    print("HELLO WORLD OF PYTHON")


say_hello()

# get_hello = info(say_hello)
# get_hello()
