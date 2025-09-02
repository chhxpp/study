#数值、字符串、元组---不可修改
#列表、集合、字典---可随时修改
import copy

print('元组变量')
c=[3]
a=[1,2,c]
b=tuple(copy.deepcopy(a))
a[0]=888
c[0]=999
print(a,list(b))

# 列表等变量
print('\t列表变量')
a=[1,2,3]
b=a
b.extend([4,5])
print(a[0])

#元组修改
print('\t元组变量')
a=[1,2,3]
b=(15,a,'abc')
c=b
a[1]=999
print(b)
print(c is b)

print('\n修改列表元素值')
price=[1000,800,1200,300]
for i in price:
    i=i+1
print(price)
#price内容没变

i=0
while i<len(price):
    price[i]=price[i]+7
    i+=1
print(price)
#price内容改变

#以下代码在脚本中和交互中行为不一致。脚本中运行都是相同的地址
#交互时[-5,256]时相同，其他值的不同
a=257
b=257
print(id(a), id(b))

#交互中，任意数都相同。
a=257;b=257
print(id(a), id(b))