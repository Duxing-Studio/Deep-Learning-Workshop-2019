s = 'string'
print(len(s))
print(s[0])  # 输出序列的第一个元素
print(s[-1])  # 输出字符串的最后一个元素
print(s[1:3])  # 输出字符串的第2-3个字符，不包含第4个字符
t = '这是个中文字符串'
print(len(t))
# 使用+运算符合并字符串
print(s + t)
# 使用*运算符复制字符传
print(s * 3)
# 使用字符串对象的内置方法
print(s.find('in'))
print(s.replace('g', 'gs'))  # 虽然显示字符串已被替换，但实际上是一个新的字符串。
# 字符串类型是不可变性类型
print(s)
# 得到字符串对象所有的属性和方法
print(dir(s))
# 内置的帮助函数
print(help(s.upper))
# s[0] = 'another s'
# print(s)
s = "yangjh"
for i in s:
    print(i, end="")
