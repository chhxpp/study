from functools import partial


def myfun():
    print('函数自己输出的hello')
    return

a=myfun()
print('显示a变量:',a)
print('执行myfun()的结果是：',myfun())
print('只显示myfun，无括号:',myfun)
print('a的类型是',type(a))
print(id(a))
print(id(myfun))
print(id(myfun()))
print(id(None))
print(id(print))

x=['博士','硕士','圣斗士','学士']
def degree_order(s):
    if s=='学士':return 0
    elif s=='硕士':return 1
    elif s=='博士':return 2
    elif s=='圣斗士':return 3
    else:return -1

s=sorted(x,key=degree_order)
print(s)

def f(s):
    return len(s)<3

b=filter(f,x)
print(list(b))

from functools import partial
pi=3.1415926
print('系统的round',id(round))
add=id(round)
round=partial(round,ndigits=2)
print('自己定义的round',id(round))
print(round(pi))

import ctypes

# 假设原始 round 的地址是 1771239433904（需替换为你的实际地址）
original_round_addr = add

# 将地址转换为函数对象
original_round = ctypes.cast(original_round_addr, ctypes.py_object).value

# 调用原始函数
pi = 3.1415926
print(original_round(pi))  # 输出: 3.141593

def oo(s):
    return s%2==0

x=[2,6,8,9,13,16]
y=filter(oo,x)
print(list(y))
