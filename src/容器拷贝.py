from copy import deepcopy
a=[1,[2,3,],4]
b=a.copy()
print(b)
a[1][0]='已'
print(a,b)
c=deepcopy(a)
a[1][1]='小'
print(a,c)

a=[0,0,0]
b=[a]*2
print(b)
a[1]=999
print(a,b)

print(id(a),id(b[0]),id(b[1]))
