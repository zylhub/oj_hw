# coding=utf-8
def solution(I, R):
	m = int(I[0])
	I_lst = I[1:]
	R_lst = R[1:]
	R_lst = list(set(R_lst))  # 去重
	R_lst.sort()
	n = len(R_lst)
	ret = []
	for i in range(n):
		flag = False
		count = 0
		rule = R_lst[i]
		for j in range(m):
			if str(rule) in I_lst[j]: # 判断是否包含
				flag = True
				count += 1
				ret.append(j)
				ret.append(I_lst[j])
		if flag is True:
			ret.insert(-count * 2, rule)
			ret.insert(-count * 2, count)
	ret.insert(0, len(ret))  # 插入长度
	ret_len = len(ret)
	# 格式最后一个输出后换行
	for k in range(ret_len):
		if k < ret_len - 1:
			print ret[k],
		else:
			print ret[k]


import sys

try:
	while True:
		line_one = sys.stdin.readline().strip()
		if line_one == '':
			break
		line_two = sys.stdin.readline().strip()
		I = line_one.split()
		R = map(int, line_two.split())
		solution(I, R)
except:
	pass
