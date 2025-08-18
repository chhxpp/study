A = [1, 2, 3, 4, 5]
print('初始列表:', A)

# 添加元素
A.append(6)
print('append 6:', A)
A.insert(0, 0)
print('insert 0 at index 0:', A)
A.extend([7, 8])
print('extend [7, 8]:', A)

# 删除元素
A.remove(3)
print('remove 3:', A)
del A[0]
print('del index 0:', A)
pop_val = A.pop()
print('pop():', A, '弹出值:', pop_val)

# 修改元素
A[0] = 100
print('修改index 0为100:', A)

# 查找元素
index_4 = A.index(4)
print('index of 4:', index_4)
count_2 = A.count(2)
print('count of 2:', count_2)

# 排序和反转
A.sort()
print('排序:', A)
A.reverse()
print('反转:', A)

# 清空
A.clear()
print('清空:', A)
