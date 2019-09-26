a = [2, 2, 2]
# 修改列表元素内容
a[1] = 1
print(a)
# 删除列表元素
del a[1]
print(a)
# 分片赋值
name = list('Python')
print(name)
name[2:] = list('data')
print(name)
# 分片赋值用于插入元素
name[1:1] = list('--')
print(name)
# 追加方法
code = [1, 2, 3]
code.append(4)
print(code)
# 计数方法
code = ['to', 'be', 'or', 'not', 'to', 'be']
print(code.count('to'))
# 追加方法
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
b + [7, 8, 9]
print(b)
# 索引
a = [1, 2, 3, 3, 2, 1]
print(a.index(1))
# 插入
a = [1, 2, 3]
a.insert(2, 2.5)
print(a)
# pop
a = [1, 2, 3]
print(a.pop())
print(a)
print(a.pop(0))
print(a)
# remove
code = ['to', 'be', 'or', 'not', 'to', 'be']
print(code.remove('or'))
print(code)
# reverse
a = [1, 2, 3]
a.reverse()
print(a)
# sort
a = [1, 3, 4, 8, 6, 2]
a.sort()
print(a)
