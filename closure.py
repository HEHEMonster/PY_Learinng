# 闭包
def Func1(): 
    x = 5
    def Func2():
        x *= x
        return x
    return Func2


# 容器类型    列表的值不是存放在栈里 
def Func3(): 
    x = [5]
    def Func4():
        x[0] *= x[0]
        return x[0]
    return Func2()

# nolocal关键字
def Func6(): 
    x = 5
    def Func2():
        nonlocal x
        x *= x
        return x
    return Func2()


# function 
print(type(Func1()))

close(5)(3)

