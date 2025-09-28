from pathlib import Path
import shutil
from datetime import datetime

root=Path(r'd:\mydoc\py\study-py\src')
#print(root)

exclude_dirs = ['__pycache__','test']  # 要排除的文件夹列表
p=root/ 'test'
p.mkdir(exist_ok=True)

p1=[]#文件名后缀
p2=[]#文件全路径
file_list=root.rglob('*.*')

for f in file_list:
    #print(f.parts)
    if not any(exclude_dir in f.parts for exclude_dir in exclude_dirs):
        p1.append(f.suffix[1:])
        p2.append(str(f))
        p=root/ 'test'/ f.suffix[1:]#生成的新文件夹放到test目录下，便于集中观察和删除。
        p.mkdir(exist_ok=True)
        ct=datetime.fromtimestamp(f.stat().st_mtime).strftime('%y%m%d')#mtime为最后修改时间，ctime似乎被弃用了。
        shutil.copy(f, p/f'{f.stem}_{f.parent.stem}_{ct}{f.suffix}')#文件名形如：赛马_src_250916.py

print('\n文件名后缀为：')
print('\n'.join(str(file) for file in set(p1)))

print('\n全路径文件名称为：')
print('\n'.join(str(file) for file in p2))



