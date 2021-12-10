import pandas as pd
import matplotlib.pyplot as plt

# 读取目标文件并保存为DataFrame对象
dataframe = pd.DataFrame(pd.read_excel('2009-2014年度改判发回案件总体情况.xlsx'))
# 将DataFrame对象表头转化为numpy对象
columns_numpy = dataframe.columns.to_numpy()
# 保存DataFrame对象的数据域
values_numpy = dataframe.values
# 初始化一个字典
data_dict = dict()
# 将表头存放在字典中
data_dict['年份'] = columns_numpy[1:]
# 遍历DataFrame对象的数据域
for i in range(len(values_numpy)):
    data_dict[values_numpy[i][0]] = values_numpy[i][1:]
pd.DataFrame(data_dict).plot(x='年份', kind='bar')
# 设置字体中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  
# 设置x轴标签名称
plt.xlabel('年份') 
# 设置y轴标签名称
plt.ylabel('改判情况')  
 # 设置柱状图的标题
plt.title('2009-2014年度改判发回案件总体情况', fontsize=14) 
# 设置图例的位置
plt.legend(loc=2, bbox_to_anchor=(1.05,0.4))
# 保存图片到指定位置
plt.savefig('2009-2014年度改判发回案件总体情况.png',dpi=600,bbox_inches='tight')