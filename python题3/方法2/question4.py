import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame(pd.read_excel(r"D:\桌面\Python数据分析与处理-试题 (3)\超市营业额2.xlsx"))
df = df.drop_duplicates()  # 删除重复行
for i in df[df['交易额'].isnull()].index:  # 缺失值填充
    df.loc[i, '交易额'] = round(df.loc[df.姓名 == df.loc[i, '姓名'], '交易额'].mean())
# 小于100的一律赋值为100
df.loc[df.交易额 < 100, '交易额'] = 100
# 大于5000的一律赋值为5000
df.loc[df.交易额 > 5000, '交易额'] = 5000
dt = (pd.DataFrame(df.groupby(by='姓名').sum()['交易额']).sort_values(by='交易额')).to_dict()  # 将交易额按名字分组总和并升序排列后转为字典
s_list: dict = dt['交易额']  # 取出交易额对应字典
list1 = list(s_list.keys())  # 将字典的键转化为列表
list1.reverse()  # 列表逆置
print("按员工业绩从高到低进行排序为：")
for name in list1:  # 按列表顺序输出字典数据
    value = s_list.get(name)
    print("员工名：", name, "，总业绩：", value)
# 将数据按姓名及日期分组并求和
dff: pd.DataFrame = (df.groupby(by=['姓名', '日期'], as_index=False).sum())
# 打印每个员工每天的业绩透视表
print("每个员工每天的业绩透视表为：")
print(dff.pivot(index='姓名', columns='日期', values='交易额'))
# 将数据按姓名及柜台分组并求和
dff = (df.groupby(by=['姓名', '柜台'], as_index=False).sum())
# 打印每个员工在每个柜台的业绩透视表
print("每个员工在每个柜台的业绩透视表为：")
print(dff.pivot(index='姓名', columns='柜台', values='交易额'))
