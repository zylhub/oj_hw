from collections import OrderedDict


def solution(lines):
	records = OrderedDict()
	for line in lines:
		name, num = line.split()
		name = name.split('\\')[-1]
		if (name, num) not in records:
			records[(name, num)] = 1
		else:
			records[(name, num)] += 1
	return records


import sys

try:
	while True:
		print "lines"
		lines = sys.stdin.readlines().strip()
		print lines
		if not lines:
			break
		ret = solution(lines)
		print ret
		result = sorted(ret.iteritems(), key=lambda x: x[1], reverse=True)
		print result
		for e in result[:8]:
			print e[0][0][-16:], e[0][1], e[1]
except:
	pass
