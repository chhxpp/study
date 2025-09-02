with open('股票.txt','r') as f:
    s=f.readlines()

new=[i.split(',') for i in s[1:]]
key=[[x[1],float(x[5]),int(x[6].strip())] for x in new ]
high=[i for i in key if i[2]>10000]

print(high)