import xlwings as xw

app=xw.App(add_book=False)
app2=xw.App(add_book=False)
wb1=app.books.open(r'D:\mydoc\projs\py\res\doc\temp.xlsx')
wb2=app2.books.open(r'D:\mydoc\projs\py\res\doc\temp2.xlsx')
wb=app.books['temp.xlsx']
wb.sheets[0].range('A1').value='hello'