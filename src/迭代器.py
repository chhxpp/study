a=[10,20,30]
b=[1,2,3]

#x=(i*k for i in a for k in b )
x=zip(a,b)
for i in range(0):
    next(x)
print(next(x))