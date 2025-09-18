from pathlib import Path
root=Path(r'd:\mydoc\py\study-py\src')
exclude_dirs = ['venv', '__pycache__', '.git']  # 要排除的文件夹列表

p1=[]
for f in root.rglob('*.*'):
    #print(f.parts)
    if not any(exclude_dir in f.parts for exclude_dir in exclude_dirs):
        p=f.suffix[1:]
        p1.append(p)
p1=list(set(p1))
print(p1)
for p in set(p1):
    p= root / p
    p.mkdir(exist_ok=True)