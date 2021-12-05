# 导入pandas模块并以pd名称使用
import pandas as pd

# 设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 读取EXCEL文件‘超市营业额2.xlsx’
df = pd.DataFrame(pd.read_excel(r"D:\桌面\试题\试题\python试题3\超市营业额2.xlsx"))
# 删除重复行
df = df.drop_duplicates()  
# 用该员工的平均销售额并用round将数据四舍五入后进行缺失值填充
for i in df[df['交易额'].isnull()].index:  
    df.loc[i, '交易额'] = round(df.loc[df.姓名 == df.loc[i, '姓名'], '交易额'].mean())
# 交易额小于100的数据一律赋值为100
df.loc[df.交易额 < 100, '交易额'] = 100
# 交易额大于5000的一律赋值为5000
df.loc[df.交易额 > 5000, '交易额'] = 5000
# 将交易额按名字分组汇总并按交易额升序排序
dff = df.groupby(by='姓名')['交易额'].sum().sort_values()
# 将dff的数据转化为字典
df_dict = dff.to_dict()
# 将字典的键即员工姓名数据转化为列表
df_list = list(df_dict.keys()) 
# 将df_list逆置，本是升序排序，逆置后即为降序排序时姓名的排序
df_list.reverse()
print("按员工业绩从高到低进行排序后的结果为：")
# 按列表顺序输出字典数据
for n in df_list:  
    # 在字典中获取营业额
    v = df_dict.get(n)
    print("员工", n, "的总营业额为", v,"元")
# 将数据按姓名及日期分组并求和
ddf = df.groupby(by=['姓名', '日期'], as_index=False).sum()
# 打印每个员工每天的业绩透视表
print("每个员工每天的业绩透视表为：")
print(ddf.pivot(index='姓名', columns='日期', values='交易额'))
# 将数据按姓名及柜台分组并求和
ddf = df.groupby(by=['姓名', '柜台'], as_index=False).sum()
# 打印每个员工在每个柜台的业绩透视表
print("每个员工在每个柜台的业绩透视表为：")
print(ddf.pivot(index='姓名', columns='柜台', values='交易额'))
