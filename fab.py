# 递归算法
# 兔子 斐波那数列

def fab(n) :
    if n == 1 or n == 2:
        return 1
    else :
        return fab(n-1) + fab(n-2)


print('共计有%d只兔子诞生了' % fab(1))


# 汉诺塔
def hannoi(n,x,y,z):
    if n== 1 :
        print(x,'-->',z)
    else :
        haoni(n-1, x, z , y) # 将N-1个盘子从X移动到Y上
        print(x,'-->', z) # 将最底下一个盘子从x移动到z上
        haoni(n-1,y ,x ,z) # 将N-1个盘子移动到Z上
    
    hannoi(3,'X','Y','Z')