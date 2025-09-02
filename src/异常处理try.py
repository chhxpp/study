try:
    a='为'
    b=0
    print(a/b)
except ZeroDivisionError:
    print("错误：除数不能为零！")
except TypeError:
    print("错误：变量类型错误！")
finally:
    print('程序结束')