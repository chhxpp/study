from math import  sin
from random import randint

p=[250,170,300,240]
p=[i+7 for i in p]
print(p)

a=[1,2,3,4,5,6,7,8,9,10]
b=[sin(x) for x in a]
c=[int(x*100)/100 for x in b]
print([int(x*100)/100 for x in b])

a=[randint(1,1000) for k in range(10)]
print(a)