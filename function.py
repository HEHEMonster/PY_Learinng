# 函数 Python的乐高积木

# 定义

def MyFirstFunction():
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