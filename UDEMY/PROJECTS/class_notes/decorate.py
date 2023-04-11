def validate(f):
    def valid(x,y):
        if x < 0 or y < 0:
            raise ValueError("X or Y = negative number")
        else:
            return f(x,y)
    return valid


@validate #everytim i call sum, validate is executed firts
def sum(x,y):
    return x+y

print(sum(10,20))
