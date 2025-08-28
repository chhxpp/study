import chardet

file='./src/t1.txt'

with open(file, 'rb') as f:
    s=f.read()

d=chardet.detect(s)
e=d['encoding']
print(d)

with open(file, 'r', encoding=e) as f:
    s=f.readlines()

for i in s:
    print(i)