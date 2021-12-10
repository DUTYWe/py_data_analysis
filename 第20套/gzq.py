# question1

# 从标准输入获取一个列表
integer_list = eval(input("输入一个列表："))  
# 创建一个存储符合要求的数据的列表
result_list = list()  
# 循环遍历输入列表
for integer in integer_list:  
     # 如果列表中的数据以2取余为0，说明符合要求
    if integer % 2 == 0:
        # 将符合要求的数据附加到结果列表后 
        result_list.append(integer)  
print(result_list)

# question2

# 创建存储结果数据的列表
result_list = list()  
 # 由于1既不是质数也不是素数，只需要遍历2-100之间的数字
for integer in range(2, 100): 
    tmp = 2
     # 遍历2-i之间的数字，判断i是否会被除本身以外的其他数字整除
    for tmp in range(2, integer): 
        # 如果存在除本身以外的其他数字整除，则不符合要求
        if integer % tmp == 0:
            break  
     # 如果不存在除本身以外的其他数字整除
    else: 
        result_list.append(integer) 
print(result_list)  


# question3

import sys

equation = str(input("输入一个一元二次方程，格式为ax^2+bx+c=0(a!=0)："))
a, b, c = 0, 0, 0
 # 判断输入中是否存在二次项
if 'x^2' not in equation: 
    print("这个方程式没有二次项")
    # 如果没有，程序退出
    sys.exit()  
# 用“=”分割方程，判断方程是否存在问题，如果不存在问题则取出需要的数据
equation_list = equation.split("=")
# 如果列表长度不等于2，则说明方程组有问题
if len(equation_list) != 2:
    print("你输入的不是一个方程")
    sys.exit()
else:
    equation = equation_list[0]
# 取出方程中的二次项
# 如果没有截取之后长度为0，则二次项系数为1
if len(equation[:equation.index('x^2')]) == 0:
    a = 1
# 如果没有截取之后长度为1且为“=”，则二次项系数为-1 
elif len(equation[:equation.index('x^2')]) == 1 and equation[0] == "-":
    a = -1
else: 
    a = int(equation[:equation.index('x^2')])
equation = equation[equation.index('x^2') + 3:]
# 判断二次项及运算符之后的字符串中是否存在一次项
if 'x' in equation:
    # 如果第一位是加号，就去掉第一位
    if equation[0] == "+":
        equation = equation[1:]
    # 如果没有截取之后长度为0，则一次项系数为1 
    if len(equation[:equation.index('x')]) == 0:
        b = 1
    # 如果长度目标长度是1且为“=”
    elif len(equation[:equation.index('x')]) == 1 and equation[0] == "-":
        b = -1
    else:
        # 取出方程一次项的系数
        b = int(equation[:equation.index('x')])
    equation = equation[equation.index('x')+1:]
# 如果第一位是加号，就去掉第一位
if equation[0] == "+":
        equation = equation[1:]
if len(equation) == 0:
    c = 0
else:
    # 如果存在一次项，则取出常数项
    c = int(equation)  
# 根据方程根的判别式判断根的情况
if (b * b - 4 * a * c) > 0:
    print("此方程有两个不相等的实数`根")
elif (b * b - 4 * a * c) == 0:
    print("此方程只有一个实数根")
else:
    print("此方程没有实数根")

# 问题四

import openpyxl as opl

# 将数据记录入元组中
data = (('月份', '1', '2', '3', '4', '5', '6'),
              ('张三', '51', '32', '58', '57', '30', '46'),
              ('李四', '70', '30', '48', '73', '82', '80'),
              ('王五', '60', '40', '46', '50', '57', '76'),
              ('赵六', '110', '75', '130', '80', '83', '95'))
# 在xlsx文件中创建一个工作簿
wb = opl.Workbook()
# 选择文件中默认的工作表
st = wb.active
st.title = '某商场各销售员业绩（万元）'
# 获取数据的行数
Rows = len(data)
# 获取数据的列数
Cols = len(data[0])
# 遍历元组，将数据写入单元格
for row in range(Rows):
    # 列号从‘A’开始
    colid = 'A'
    for col in range(Cols):
        # 将数据写入单元格
        st['%s%d' % (colid, row + 1)] = data[row][col]
        # 列号调整为为下一个ASCII字母
        colid = chr(ord(colid) + 1)
# 将内存中的工作簿对象保存到磁盘上
wb.save('D:/pythontest/某商场前半年的业绩情况.xlsx')

# 问题5的解法
import pandas as pd
import matplotlib.pyplot as plt

# 读取xlsx文件
df = pd.DataFrame(pd.read_excel('D:/pythontest/某商场前半年的业绩情况.xlsx', sheet_name='某商场各销售员业绩（万元）', nrows=7, usecols='A:G'))
# 将表格的表头转为列表
header = df.columns.tolist()
# 将表头数据转为int类型，因为第一个数据为‘月份’，所以索引从1开始
head_data = list(map(int,header[1:]))
# 初始化一个字典
record = dict()
# 将表头数据放入字典中
record[header[0]] = head_data
# 获取dataframe对象的数据部分
value_list = df.values
# 遍历数据部分并将其添加到字典中
for value in value_list:
    record[value[0]] = list(value[1:])
# 用包含数据的字典重新构造一个dataframe对象
data_frame = pd.DataFrame(record)
# 绘制柱状图，指定月份为x轴
data_frame.plot(x='月份', kind='bar')
# 设置字体中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  
# 设置x轴标签
plt.xlabel('月份') 
# 设置y轴标签
plt.ylabel('营业额（万元）')  
 # 设置柱状图标题
plt.title('某商场前半年的业绩情况', fontsize=14) 
 # 修改x轴刻度样式
plt.xticks(rotation=0) 
# 保存图片到指定位置
plt.savefig('D:/桌面/某商场前半年的业绩情况.png',dpi=600)   
