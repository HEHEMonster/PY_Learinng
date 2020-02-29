# 函数 Python的乐高积木

# 定义
# 就算函数没有返回值 python 也换默认返回一个nonetype的null
def MyFirstFunction():
    price=5 #局部变量
    print('这是我第一次创建的函数')


def MySecondFunction(name): # 形参
    print('你好，{0}'.format(name))

# 设置参数默认值
def MyThirdFunction(number1,number2=100):
    return number1 + number2

# 收集参数
def Test(*params, number=11111):
    print('长度是'+len(params)
    print('第二个参数是'+ params[1])



# 调用函数 向上寻找
MyFirstFunction()

MySecondFunction('小甲鱼') # 实参

print(MyThirdFunction(1,2))

MyThirdFunction(number2 = 1, number1 = 2)

Test(,12,434,5457,323)


print.__doc__

help(print)



# 在函数里修改全局变量的值 python会在函数内创建一个新的和全局变量同名的局部变量
# 称为shadowing机制


code=5

# 如果一定要改变全局变量可以添加global关键字
def changecode():
    global code=10

pring(5)

# 内嵌函数

def fun1():
    print(1)
    def fun2():
        print2
    fun2()