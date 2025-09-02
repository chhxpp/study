from decimal import Decimal

def sqr(x):
    if isinstance(x,int):
        return sqr_int(x)
    elif isinstance(x,float):
        return sqr_float(x)
    elif isinstance(x,list):
        return sqr_list(x)

def sqr2(x):
    return globals()['sqr_'+type(x).__name__](x)

def sqr_int(x):
    return x*x

def sqr_float(x):
    return float(Decimal(str(x))*Decimal(str(x)))

def sqr_list(x):
    result=[]
    for i in x:
        result.append(i*i)
    return result

a=[1,2,3,4,5]
print(sqr(a))
print(sqr2(a))
print(globals()['Decimal'])

