def generator_func(n):
    for i in range(n):
        yield i  # 每次执行到这里，返回 i 并暂停

gen = generator_func(3)
try:
    for i in range(10):
        print(next(gen))

except StopIteration:
    print("迭代结束")
    
