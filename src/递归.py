def 阶乘(n):
    if n==1:
        s=1
    else:
        s=n*阶乘(n-1)
    return s

n=4
a=阶乘(n)
print(a)

#方法1
def see(l):
    out=[]
    for i in l:
        if not isinstance(i,list):
            out.append(i)
        else:
            out.extend(see(i))
            #out += see(i)
    return out

x=[1,[2,[3,4,[11,22]]]]
print(see(x))
