# 字典是映射类型
dict1 = { 'fjj':'fanjj','fkk':'fankk'}

print(dict['fjj'])


dict2 = { 1 : 'one' , 2 : 'two' }

# 创建字典 花括号创建
dict3 = {}

# 关键字创建字典 工厂函数
dict4 = dict((('F'，'FANJJ'),('K','KK')))

dict5 = dict(xx = '吃饭'，zz = '吃完饭')

dict5['yy'] = '不吃饭'

# 用法很多 具体使用参考文档
dict3.fromkeys(range(32), '赞')

dict3.keys()
dict3.values()
dict3.items()

# 尝试获取键  不存在的话不会报错 灵活
dict3.get(32)

# 查找键
32 in  dict3

# 清空字典 相比  dict = {} 好
dict3.clear()

# 浅拷贝
dict4 = dict3.copy()

#id(dict4) != id(dict3)


# 返回最后一个item
dict3.pop()
# 随机返回
dict3.popitem()

dict3.update({1:'不赞'})