def add(x,y):
    s=x+y
    return s

def main():
    global n
    n=add(2,7)
    file=__file__
    print(f'程序b运行结果是：{n}')
    print(f'程序b的__file__是:{file}')
    print(f'程序b的__name__是:{__name__}')

#if __name__=='__main__':
main()