a=[-5,0,-23,2]
b=sorted(a,key=lambda x:x if x >= 0 else -x)
print(b)

def order(s):
    if s=='学士':p=0
    elif s=='硕士':p=1
    elif s=='博士':p=2
    elif s=='壮士':p=3
    elif s=='圣斗士':p=4
    else:p=-1
    return p

names=['学士','圣斗士','博士','壮士','硕士']
names.sort(key=order,reverse=True)
print(names)

def order2(s,ddd):
    return ddd[s[1]]

d={'学士':0,'硕士':1,'博士':2,'壮士':3,'圣斗士':4}
names=[
       ['张学士','学士'],
       ['李圣斗士','圣斗士'],
       ['王博士','博士'],
       ['陈壮士','壮士'],
       ['杨硕士','硕士']
       ]
names.sort(key=lambda x:order2(x,d),reverse=False)
print(names)

def order2(s,ddd):
    return ddd[s[1]]

def func(x):
    return order2(x, d)

d={'学士':0,'硕士':1,'博士':2,'壮士':3,'圣斗士':4}
names=[
       ['张学士','学士'],
       ['李圣斗士','圣斗士'],
       ['王博士','博士'],
       ['陈壮士','壮士'],
       ['杨硕士','硕士']
       ]
names.sort(key=func,reverse=False)
e=sorted(names,key=func)
print('e:',e)
print('names:',names)

import random
print(random.sample(names,2))
random.shuffle(names)
print(names)