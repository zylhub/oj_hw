# coding=utf-8
"""
1. 比当前长度大的都要去除
2. 根据剩余中是否满足最大个数大于一般条件处理小于当前长度的值
"""
def solution(l_lst, c_lst, n):  # 输入 长度lst 和 代价lst
	all_len = set(l_lst)
	len_cast = zip(c_lst, l_lst)
	len_cast.sort()
	ret = []
	for each_len in all_len:
		tmp_mx = []
		tmp_mi = []
		tmp_count = l_lst.count(each_len)
		for e in len_cast:
			if each_len < e[1]:
				tmp_mx.append(e[0])
			elif each_len > e[1]:
				tmp_mi.append(e[0])
		if len(tmp_mx) > n - 2*tmp_count:  #2*count > n 说明 超过一半桌腿能够达到桌腿长度的最大值
			tmp_sum = sum(tmp_mx)
		else:
			tmp_mi.sort()
			tmp_sum = sum(tmp_mi[:1+n-2*tmp_count-len(tmp_mx)]) + sum(tmp_mx)
		ret.append(tmp_sum)
	return min(ret)






import sys

try:
	while True:
		line = sys.stdin.readline().strip()
		if not line:
			break
		n = int(line)
		line_2 = sys.stdin.readline().strip().split()
		line_3 = sys.stdin.readline().strip().split()
		line_2 = map(int, line_2)
		line_3 = map(int, line_3)
		# len_cast = zip(line_2, line_3)
		print solution(line_2, line_3, n)
except:
	pass
