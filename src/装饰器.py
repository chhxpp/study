def dec(func):
    def wrapper(*args, **kwargs):
        print('原函数执行前')
        print(func(*args, **kwargs))
        print('原函数执行后')
    return wrapper

@dec
def say_hello(*args):
    sum=0
    for i in args:
        if isinstance(i, (int, float)):
            sum+=i
    return f'{sum}'

say_hello(3,5,1,'a', None)




