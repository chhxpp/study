def sum(all_num):
    sum = 0
    for s in all_num:
        sum+=s
    return sum
sum=sum([1,2,3,4])
print(sum)

def show(**info):
    for key in info:  # 同时获取键和值
        print(f'{key}: {info[key]}')

i={'张三':27,'李四':18}
show(**i)