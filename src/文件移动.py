from pathlib import Path
import shutil
from datetime import datetime

src=Path(r'd:\src')
dst=Path(r'd:\dst')

d={}
for f in src.rglob('*.txt'):
    if f.stem not in d.keys() or f.stat().st_mtime > d[f.stem].stat().st_mtime:
        d[f.stem]=f

for key,value in d.items():
    print(key,':',value.stem+'_'+value.parent.name+value.suffix)
    #print(type(value))     

for f in d.values():
    shutil.copy(f, dst/ (f.stem+'_'+f.parent.name+f.suffix))