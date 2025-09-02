def addend(s=[]):
    s.append('end')
    return s

print(addend())
print(addend())

#结果居然是：['end', 'end']
#后续可变性理论相关章节再讲解

def addend(s=[]):
    s=s+['end']
    return s

print(addend())
print(addend())

price=[1000,800,1200,300]
for i in range(len(price)):
    price[i]=price[i]+7
print(price)

price=[1000,800,1200,300]
for i in price:
    i=i+7
print(price)

price=[1000,800,1200,300]
i=0
while i<len(price):
    price[i]=price[i]+7
    i=i+1
print(price)