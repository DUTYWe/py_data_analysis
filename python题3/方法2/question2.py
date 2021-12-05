li = ['alex', 'eric', 'arin']
print("列表的长度为：" + str(len(li)))
li.append('seven')  # 列表后附加‘seven’
print(li)  # 打印列表
li.insert(li.index('alex'), 'eight')  # 在‘alex’前面添加元素'eight'
li.remove('eric')  # 删掉一个值为‘eric’的元素
