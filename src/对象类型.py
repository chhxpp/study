from decimal import Decimal
def sqr(x):
    t=type(x).__name__

    if t=='int':
        result= x**2
    elif t =='float':
        s =Decimal(str(x))
        result = s*s
    elif t=='list':
        result =[]
        for i in x:
            result.append(i*i)
    
    return result

a=6
print(sqr(a))