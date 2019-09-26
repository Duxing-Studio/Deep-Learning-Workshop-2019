# 字符串也是序列
se = 'Hello Pythoner！'
# 访问序列中的第一个元素
print(se[0])
# 访问序列中的最后一个元素
print(se[-1])
# 使用分片访问一定范围的元素
print(se[0:5])
# 访问最后的若干个元素
print(se[-9:])
# 第二个索引不一定要比第1个索引的值要大，如下面的表达式将打印空集
print(se[1:1])
# 指定分片步长
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:10:2])
print(numbers[1::2])
print(numbers[::-2])
# 连接运算
hello = '你好'
name = 'yangjh'
print(hello + name)
# 序列乘法
print(hello * 3)
print([None] * 10)
# 成员资格in
print('张三' in ['张三', '李四', '王二'])
# 序列长度
print(len(numbers))
# 序列最大值、最小值
print(max(numbers))
print(max(['张三', '李四', '王二']))
print(max(['a', 'bc', 'c', 'b1']))
