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
