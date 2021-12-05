# 问题1
import random

number = '0123456789'  # 保存所有的数字
digit_list = [random.choice(number) for i in range(1000)]  # 使用random模块生成包含1000个随机数字的list
digit_dict = dict()  # 初始化一个字典保存数字出现的次数
for digit in digit_list:
    digit_dict[digit] = digit_dict.get(digit, 0) + 1  # 如果不存在digit则返回0，若存在则返回value
for k, v in digit_dict.items():  # 遍历字典，输出数字出现的次数
    print("数字", k, '出现的次数为', v, "次")

# 问题2
import random


def GuessDigit(max_digit, min_digit, times):
    """猜数游戏"""
    goal = random.randint(min_digit, max_digit)  # goal变量存储范围内随机生成的数字
    for i in range(times):
        guess_digit = int(input("输入你猜测的数字："))  # 从控制台获取猜测的数字
        if guess_digit > goal:  # 如果猜测数字比目标数字大
            print("你猜的数字太大了，请重新猜测，剩余次数：" + str(times - i - 1))
            continue
        elif guess_digit < goal:  # 如果猜测数字比目标数字小
            print("你猜的数字太小了，请重新猜测，剩余次数：" + str(times - i - 1))
            continue
        else:  # 如果猜测数字是目标数字
            print("恭喜你，猜对啦")
            break
    else:
        print("你的次数用完啦")  # 次数用完


GuessDigit(10, 2, 4)

# 问题3
import pandas


def ReadXlsx(path):
    # 设置列对齐
    pandas.set_option('display.unicode.ambiguous_as_wide', True)
    pandas.set_option('display.unicode.east_asian_width', True)
    df = pandas.read_excel(path)  # 读取全部文件数据，使用默认索引
    print("不同员工的销售总额")
    print(df.groupby(by='姓名').sum()['交易额'].apply(int))  # 员工的销售总额，并转换为整数
    print("不同时段的销售总额")
    print(df.groupby(by='时段').sum()['交易额'].apply(int))  # 每个时段的销售总额，并转换为整数
    print("不同柜台的销售总额")
    print(df.groupby(by='柜台').sum()['交易额'].apply(int))  # 每个柜台的销售总额，并转换为整数

ReadXlsx("D:\桌面\python试题6\超市营业额2.xlsx")

# 问题4
import pandas
from copy import deepcopy

df = pandas.DataFrame(pandas.read_excel(r"D:\桌面\python试题6\超市营业额2.xlsx"))  # 读取全部文件数据，使用默认索引
df_copy = deepcopy(df)
df_copy['工号'] = df['工号'].map(lambda num: str(num)[len(str(num)) - 1] + str(num))  # 将所有员工的工号前面增加原工号最后一位数字
df_copy.to_excel("超市营业额2_修改工号.xlsx")  # 保存文件

# 问题5
import pandas
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pandas.DataFrame(pandas.read_excel(r"D:\桌面\python试题6\超市营业额2.xlsx"))  # 读取全部文件数据，使用默认索引
df_dict = df.groupby(by='柜台')['交易额'].sum().to_dict()  # 获取每个柜台的销售总额并转化为字典
# 绘制饼状图
plt.pie(list(df_dict.values()),  # 每个扇形对应的数值
        labels=list(df_dict.keys()),  # 每个扇形的标签
        autopct='%1.2f%%')  # 数据百分比显示格式
plt.title("本月各柜台营业额在交易总额中的占比")  # 设置饼状图的标题
# 设置中文字体显示
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 展示饼状图
plt.show()
