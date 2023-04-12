def mult(x):
    def calc(y):
        return x*y
    return calc


dobro = mult(2)
print(dobro(25))

triplo = mult(3)
print(triplo(15))

#--------------------
#--------------------
#--------------------


def sum(x, y):
    return x + y


def mult(x, y):
    return x * y


def over(func, x):
    def inner(y):
        return func(x, y)
    return inner


x = over(sum, 5)
print(x(15))
