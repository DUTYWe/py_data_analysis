import math

side1, side2, angle = map(float, input("请输入两个边长以及它们的夹角：").split())  # 输入两个边长以及边长的夹角
side3 = round(math.sqrt(math.pow(side1, 2) + math.pow(side2, 2) - 2 * side2 * side1 * math.cos(angle*math.pi/180)),2)  # 求出第三条边
print("第三条边长为：" + str(side3))
