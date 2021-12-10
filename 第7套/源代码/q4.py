import openpyxl as opl
# 用元组存储原数据
data_tuple = (('',2009,2010,2011,2012,2013,2014),
    ('总案件数',30,31,34,26,32,22),
    ('减轻',17,21,18,10,15,13),
    ('加重',2,3,5,3,8,2),
    ('宣告无罪',5,4,3,4,2,2),
    ('发回重审',5,6,6,7,8,4),
    ('其他',1,0,1,2,0,1)
    )

# 创建一个xlsx文件工作簿
workbook1 = opl.Workbook()
# 选择文件中默认的工作表
sheet1 = workbook1.active
sheet1.title = '某商场各销售员业绩（万元）'
# 遍历元组，将数据写入单元格
for row in range(len(data_tuple)):
    # 列号从‘A’开始
    colid = 'A'
    for col in range(len(data_tuple[row])):
        # 将数据写入单元格
        sheet1['%s%d' % (colid, row + 1)] = data_tuple[row][col]
        # 列号调整为为下一个字母
        colid = chr(ord(colid) + 1)
# 将工作簿对象保存到目标位置上
workbook1.save('2009-2014年度改判发回案件总体情况.xlsx')