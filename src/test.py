from pathlib import Path
p1=Path(__file__) .parent
p2=p1 / 'data/img/草原.bmp'
print(p1)
print(list(p1.rglob('*')))