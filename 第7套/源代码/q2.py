import re
# 用dial_clean存储目标字符串
dial_clean = '15   年 已经 成为 中国 全力 推进  一带 一路  构想 的 新起点  亚欧 互联互通 的    政策 沟通  设施 联通  贸易 畅通  资金 融通  民心  相通  五大 领域 齐头并进  文化产业 国际 合作 是 亚欧 产业 互联互通 的 重要 领域  文化 贸易 是 国际贸易 中 的 重要 内容  它 涉及 货物贸易  服  务 贸易 和 知识产权 贸易  具有 极强 的 特殊性  而    一带 一路  国家 战略 的 实施 为 发展 文化 贸易 提供 了 良好 契机'
# 将字符串中的各种空格换为‘|’，正则表达式‘\s+’代表多行空格。
dial_clean = re.sub('\s+','|',dial_clean)
# 用‘|’将字符串切割为列表，并存储在list1中
list1 = dial_clean.split('|')

# print(list1)
# 初始化一个字典
tr_dic = dict()
# 遍历列表
for tr in list1:
	# 如果该字符串不存在在字典中，则将其存储
	if tr_dic.get(tr,0) == 0:
		tr_dic[tr] = 1
	else:
		# 否则将其value值加一
		tr_dic[tr] += 1
# 打印出这个字典
print(tr_dic)