# 问题1
import string
import random

x = string.digits  # 使用模块string的digits生成所有数字
y = [random.choice(x) for i in range(1000)]  # 生成包含1000个随机数字的列表
d = dict()  # 使用字典保存每个数字出现次数
for ch in y:  # 遍历list y
    d[ch] = d.get(ch, 0) + 1  # d.get(ch,0) 返回ch出现的次数，若没有返回0
for i in range(10):
    print("数字", i, "出现了", d.get(str(i), 0), "次")  # 在字典中获取数字出现的次数

# 问题2
import numpy as np  # 导入numpy模块并重命名为np


def GuessNum(max_num, min_num, freq):
    target = np.random.randint(min_num, max_num)  # 在范围内生成随机数字并用target保存
    while freq != 0:
        num = int(input("请输入你猜测的数字："))  # 从标准输入获取猜测数字
        freq -= 1  # 次数减一
        if num > target:  # 如果猜测数字比目标数字大
            print("你猜出的数字过大，还有", freq, "次机会，", "请重新猜测。")
            continue
        elif num < target:  # 如果猜测数字比目标数字小
            print("你猜出的数字过小，还有", freq, "次机会，", "请重新猜测。")
            continue
        else:  # 如果猜测数字是目标数字
            print("恭喜你，猜对了")
            break
    else:
        print("你的次数已用完，游戏结束")  # 次数用完


GuessNum(10, 5, 2)

# 问题3
import pandas as pd  # 导入pandas模块并重命名为pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel(r"D:\桌面\python试题6\超市营业额2.xlsx")  # 读取全部文件数据，使用默认索引
# 员工的销售总额
print("不同员工的销售总额".ljust(20, '='))
print(df.groupby(by='姓名')['交易额'].sum())
# 每个时段的销售总额
print("不同时段的销售总额".ljust(20, '='))
print(df.groupby(by='时段')['交易额'].sum())
# 每个柜台的销售总额
print("不同柜台的销售总额".ljust(20, '='))
print(df.groupby(by='柜台')['交易额'].sum())

# 问题4
import pandas as pd  # 导入pandas模块并重命名为pd
from copy import deepcopy

df = pd.read_excel(r"D:\桌面\python试题6\超市营业额2.xlsx")  # 读取全部文件数据
dff = deepcopy(df)  # 将df文件内容拷贝进dff中
dff['工号'] = df['工号'].map(lambda s: str(s)[-1] + str(s))  # 利用map方法修改工号
dff.to_excel("D:\桌面\python试题6\超市营业额2_修改工号.xlsx")  # 将文件保存为超市营业额2_修改工号.xlsx

# 问题5
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_excel(r"D:\桌面\python试题6\超市营业额2.xlsx"))  # 读取全部文件数据，使用默认索引
data_dict = df.groupby(by='柜台')['交易额'].sum().to_dict()  # 获取每个柜台的销售总额并转化为字典
list_label = list(data_dict.keys()) # 用list_label存储柜台类别
list_value = list(data_dict.values()) # 用list_value存储各柜台的交易总额
# 绘制饼状图
plt.pie(list_value, labels=list_label, autopct='%1.1f%%',frame=0)
plt.title("本月各柜台交易额情况饼状图")  # 设置饼状图的标题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体中文显示
plt.show()  # 展示饼状图
