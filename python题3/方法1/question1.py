# 导入math模块
import math

# 输入两个边长a,b以及边长的夹角b
s1, s2, c = map(float, input("请输入两个边长以及它们的夹角：").split())  
# 根据余弦定理求出第三条边，利用pi常量将角度转化为弧度，round函数用于结果取两位小数
s3 = round((s1**2 + s2**2 - 2 * s1 * s2 * math.cos(c*math.pi/180))**0.5,2)  
print("第三条边长为：",s3)