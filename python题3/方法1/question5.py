# 导入matplotlib模块以及模块中的pyplot包
import matplotlib.pyplot as plt
import matplotlib as mpl

# 将数据存入字典中
data_dit = {'蔬菜': [1350, 1500, 1330, 1550, 900, 1400, 980, 1100, 1370, 1250, 1000, 1100],
            '水果': [400, 600, 580, 620, 700, 650, 860, 900, 880, 900, 600, 600],
            '肉类': [480, 700, 370, 440, 500, 400, 360, 380, 480, 600, 600, 400],
            '日用': [1100, 1400, 1040, 1300, 1200, 1300, 1000, 1200, 950, 1000, 900, 950],
            '衣服': [650, 3500, 0, 300, 300, 3000, 1400, 500, 800, 2000, 0, 0],
            '旅游': [4000, 1800, 0, 0, 0, 0, 0, 4000, 0, 0, 0, 0],
            '随礼': [0, 4000, 0, 600, 0, 1000, 600, 1800, 800, 0, 0, 1000]}

# 初始化两个列表，v_list用于存储数据，t_list用于存储消费类型
v_list = list()
t_list = list()
# 遍历字典，将数据存储在两个列表中
for k,v in data_dit.items():
    t_list.append(k)
    v_list.append(sum(v))
# 绘制饼状图，第一个参数是每个扇形对应的数值，labels参数是每个扇形的标签，autopct是数据百分比显示格式
plt.pie(v_list,  labels=t_list, autopct='%1.2f%%') 
 # 设置饼状图的标题
plt.title("家庭全年各个类别花销情况饼状图")  
# 设置中文字体显示
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False
# 展示饼状图
plt.show()
