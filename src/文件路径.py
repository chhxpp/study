from pathlib import Path
root=Path(r'd:\mydoc\py\study-py\src')
exclude_dirs = ['venv', '__pycache__', '.git']  # 要排除的文件夹列表

p1=[]#文件名后缀
p2=[]#文件全路径
r=list(root.rglob('*.*'))
for f in r:
    #print(f.parts)
    if not any(exclude_dir in f.parts for exclude_dir in exclude_dirs):
        p1.append(f.suffix[1:])
        p1=list(set(p1))
        p2.append(str(f))
print('文件名后缀为：\n',p1)
#print('文件名称为：',[p.name for p  in r])
print('全路径文件名称为：')
print('\n'.join(str(file) for file in p2))
#创建目录
for p in set(p1):
    p= root / p
    #p.mkdir(exist_ok=True) #生成目录稳定有效，为避免每次运行都生成测试的目录，暂时注释掉