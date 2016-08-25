#coding=utf-8

path = [i for i in xrange(10001)]
def find_path(x):
	y = path[x]
	while y != path[y]:
		y = path[y]
	path[x] = y
	return y

def solution(inp, inp_str, n):
	inp_str = list(inp_str)

	for i in range(n):
		x , y = inp[i]
		a = find_path(x)
		b = find_path(y)
		if a<b:
			path[b] = a
		else:
			path[a] = b
	# print path

	for i in range(n):
		for j in range(i+1,n):
			if find_path(i)==find_path(j) and inp_str[i] > inp_str[j]:
				inp_str[i], inp_str[j] = inp_str[j], inp_str[i]
	return ''.join(inp_str)


def solution_(line, inp, n):
	"""局部数据进行调整
	1）根据输入找到那些是需要排序的下标
	2） 分组排序
	"""
	inp = list(inp)
	idx = []
	visited = [False for i in range(n)]
	for i in range(n - 1):
		if not visited[i]:
			a_set = set(line[i])
			for j in range(i + 1, n):
				b_set = set(line[j])
				if a_set & b_set:
					a_set = a_set.union(b_set)
					visited[j] = True
			#print 'a_set',a_set
			idx.append(list(a_set))
		else:
			continue
	print idx
	for ix in idx:
		ix.sort()
		tmp = [inp[int(i)] for i in ix]
		tmp_sorted = sorted(tmp)
		for i, k in enumerate(ix):
			inp[int(k)] = tmp_sorted[i]

	return ''.join(inp)


import sys

try:
	while True:
		inp_str = sys.stdin.readline().strip()
		if not inp_str:
			break
		n = sys.stdin.readline().strip()
		n = int(n)
		inp = []
		for i in range(n):
			inp_line = sys.stdin.readline().strip()
			inp.append(map(int, inp_line.split()))
		print solution(inp, inp_str, n)
except:
	pass