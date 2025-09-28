from os.path import exists
filename = 'D:/file.txt'
a=2
try:
    with open(filename) as f:
        s=10/a
    #kdkjfkj
except ZeroDivisionError as zde:
    print('错误：零不能做被除数')
except FileNotFoundError as fnfe:
    print('错误：指定的文件不存在') 
except Exception as e:
    print('发生意外',e)
else:
    print('没有发生异常')
finally:
    print('无论是否发生异常，都会执行的代码')