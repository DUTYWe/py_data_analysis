# 用li存储原数据
li = ['alex', 'eric', 'arin']
# 利用内置函数len获取列表长度
print("列表的长度为：",len(li))
# 在列表li后附加‘seven’
li.append('seven')  
# 输出添加‘seven’后的列表li
print(li)  
# 在‘alex’前面添加元素'eight',利用index函数获取‘alex’的位置
li.insert(li.index('alex'), 'eight')  
# 删掉一个值为‘eric’的元素
li.remove('eric')  