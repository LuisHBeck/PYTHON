def mult(x):
    def calc(y):
        return x*y
    return calc


dobro = mult(2)
print(dobro(25))

triplo = mult(3)
print(triplo(15))
