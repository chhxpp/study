#求各键出现次数
a=['A','B','C','A','A','B']
b=[a.count(x) for x in a]
c=dict(zip(a,b))
print(c)

d={x:a.count(x) for x in set(a)}
print(d)

d={}.fromkeys(a,0)
for i in d:
    print(i,d[i],a.count(i))
e={i:a.count(i) for i in d}
print(e)

g={x:a.count(x) for x in a if  a.count(x)>1}
print(g)

h=['美国','法国','俄罗斯']
i=['Uk','FRA','RUS']
j={x:y for x in h for y in i}
k={x[0]:x[1] for x in zip(a,b)}
print (k)

#求出现的各次数，出现的次数
a=['A','B','C','A','A','B','B']
d={i:a.count(i) for i in a}
d2={k:list(d.values()).count(k) for k in d.values()}
print(d2)

#求众数
a=['A','B','A','C','B','C','B','C','B']
d={i:a.count(i) for i in a}
m=max(d.values())
d2={i:d[i] for i in d if d[i]==m}
print(d2)

#反向索引
a={'A':1,'B':2,'C':3}
b={y:x  for x,y in a.items()}
print(b)

