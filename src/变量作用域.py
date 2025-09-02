
def f(x):
    global a
    a=a+4
    return a

a=1
s=f(a)
print(s)
print(a)