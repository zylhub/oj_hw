def cmp(a, b):
	if a.lower() > b.lower():
		return 1
	elif a.lower() < b.lower():
		return -1
	else:
		return 0




def solution(line):
	alpha = []
	ret = [0] * len(line)
	for i in range(len(line)):
		if line[i].isalpha():
			alpha.append(line[i])
		else:
			ret[i] = line[i]
	alpha.sort(cmp)
	k = 0
	for i in range(len(line)):
		if ret[i] == 0:
			ret[i] = alpha[k]
			k += 1
	# print ret
	return ''.join(ret)


import sys

try:
	while True:
		line = sys.stdin.readline().strip()
		if not line:
			break
		print solution(line)
except:
	pass
