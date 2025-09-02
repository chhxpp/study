import xlwings as xw
import random

d={'学士':0,'硕士':1,'博士':2,'壮士':3,'圣斗士':4}

def order(t):
     s=t[1]
     return d[s]

# 单次启动 Excel，批量读取数据
with xw.App(visible=False) as app:
    wb = app.books.open('学位名单.xlsx')
    names = wb.sheets['Sheet1'].range('B3:C16').value
    a=[]+names
    b=names.copy()
    c=sorted(names,key=order)
    wb.close()  # 显式关闭工作簿

names.sort(key=order)
random.shuffle(names)

for n in names:
    print(n)

pickout=random.sample(names,1)
for n in pickout:
    print('\n',n)

