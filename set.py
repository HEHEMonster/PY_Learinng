# 集合 特色唯一
set1 = {1,2,3,4,5}

temp = []
for item in set1
    if item not in set1
        temp.append(item)


# 自动去重
set2 = set([1,2,3,4,5,6,6]) 

print(set2)

set2.add(7)
set.remove(7)


# 不可变集合
set3 = frozenset([1,2,3])
# 代码会报错
set.add(0)