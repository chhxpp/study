from decimal import Decimal

a=24
b=1.2
print(a*b)
c=Decimal(str(a))*Decimal(str(b))
d=float(c)+0.3
e=c+1
print(d)
print(format(25.369,'<10.2f'))#只改变显示。并不改变精度。
print(format(25.369,'^10.2f'))
print(format(25.369,'>10.2f'))
print(format(25.369,'>10.2e'))

print(1/float('inf'))
