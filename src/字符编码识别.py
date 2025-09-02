import chardet
file='字符编码案例.txt'

#转换成bytes类型
with open(file,'rb') as f:
    s=f.read()
print(type(s))

#识别编码
d=chardet.detect(s)
e=d['encoding']
print(d)
print('侦测到的编码是：',e)

if e.lower().startswith('gb'):
    a='gb18030'

#用正确的编码解码成字符
s2=s.decode(e)
print(s2)

#将字符按需要编码后，生成新的bytes并写入文件
t=s2.encode('ANSI')
with open('重新编码.txt','wb') as f:
    f.write(t)
