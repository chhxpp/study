from math import *
from functools import  partial,reduce

def mysin(x):
    return round(sin(x),2)

x=[0,1,2,3,4,5,6,7,8,9]
a=map(sin,x)
a2=map(lambda x:round(sin(x),2),x)
b=map(partial(round,ndigits=2),a)
from itertools import tee; b, b_copy = tee(b)
d=list(b)

print(d)
print('迭代器对象，引用一次后数据全部销毁：',list(b))
print('列表对象不受影响:',d)
print('通过lambda表达式：',list(a2))

def myadd(x,y):
    return x+y
print(reduce(myadd,[1,2,3,4],0))

def mymult(x,y):
    return x+y*y
print(reduce(mymult,[1,2,3,4],0))

c=['关羽','张飞','赵云','马超','黄忠']
print(reduce(lambda x,y:x+y[0],c,''))