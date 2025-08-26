a=[['aa','rrr',33],['bb','ttt',456],['cc','yyy',89]] 
d={x[0]:x[2] for x in a}
print(d)

a=['A','B','A','C','B','A']
d={}.fromkeys(a,0)

d={k:d[k]+1 for k in a}
print(d)