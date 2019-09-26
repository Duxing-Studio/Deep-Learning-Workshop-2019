def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    print(result)

sum(1, 10)


def sumReturn(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result

a = sumReturn(1, 5)
print(a)


def sum2(start, end):
    if(start > end):
        print("start should be less than end")
        return    # here we are not returning any value so a special value None is returned
    result = 0
    for i in range(start, end + 1):
        result += i
    return result

s = sum2(110, 50)
print(s, type(s))

global_var = 12         # 定义全局变量global_var
xy = 100								# 定义全局变量xy


def func():
    local_var = 100			# 定义局部变量local_var
    xy = 200						# 定义局部变量xy
    print(global_var)		# 可以在函数内部访问全局变量
    print(xy)						# 此时访问的是局部变量xy

func()                  # 调用函数func()

# print(local_var)      # 无法访问局部变量local_var

t = 1


def increment():
    global t   	# 现在的变量t在函数内外都是一致的
    t = t + 1
    print(t) 		# 输出 2


increment()
print(t)  # 输出 2


def named_args(name, greeting):
    print(greeting + " " + name)

named_args(name='jim', greeting='Hello')
named_args(greeting='Hello', name='jim')
named_args('jim', greeting='hello')


def bigger(a, b):
    if a > b:
        return a, b
    else:
        return b, a

s = bigger(12, 100)
print(s)
print(type(s))
