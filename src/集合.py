from collections import Counter

a=['东风','西风','东风','南风',(1,2)]
s=set(a)
print(type(s))
print(s)

a={'a':1,'b':2,'c':3}
x=set(a)
print(x)

a=['中国','美国','英国']
b=['CHN','USA','UK']
c=zip(a,b)
s=list(c)
print(s)

a={'A','B','C','D'}
b={'E','F','G','H'}
c=a&b
d=a|b
e=a-b
f=b-a
print('交集c',type(c),c)
print('并集d',type(c),d)
print('差集e=a-b',type(c),e)
print('差集f=b-a',type(c),f)
if not c:
    print('c是空集')

print(Counter(a))

a=['A','B','B','A','A']
b=['A','B','C','D','E']
a1=Counter(a)
b1=Counter(b)
c1=a1+b1
c2=a1-b1
print('counter类型',type(c),c1)
print('counter类型',type(c),c2)

a=[[1,5],[3,4],[2,1,3]]
print(max(a))

c=[max(x) for x in a]
print(max(c))

from itertools import chain
a=[1]
b=[2]
c=[3,4]
d=chain(a,b,c)
e=list(d)
print(type(e),e)

#*a解包
a=[[1,5],[3,4],[2,1,3]]
x=list(chain(*a))
print(x)