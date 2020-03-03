# lambda 表达式

def func1(x):
    return 2 * x + 1

# lambda 写法
f =lambda x : 2 * x + 1

print(f(1))

# 多参数
f1 = lambda x, y : x * y + 1

# 作用 使代码简洁
# 不需要考虑名命


# 将lambda表达式用于bIF

temp = range(10)

def odd(x):
    return x % 2

# 会自动过滤掉0和 false
filter(None,[0,1,False,True])

# [1,3,5,7,9]
list(filter(odd,temp))

list(filter(lambda x :x % 2, temp))

# map 遍历列表 
map(lambda y: y *2, [0 , 1 , 2])
