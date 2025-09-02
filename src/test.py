
def out(x):
    def inn(y):
        return x+y
    return inn

c=out(10)
print(c(5))
