# coding=utf-8

def match(p, i, s, j):
	"""
	p: 匹配模式
	s: 待匹配字符串
	i,j当前匹配字符的下标
	匹配完毕之后，i,j应该等于各自长度
	"""
	if len(p) == i and len(s) == j:
		return True
	elif len(p) <= i or len(s) <= j:
		return False
	elif p[i] == s[j]:
		return match(p, i + 1, s, j + 1)
	elif p[i] == '*':
		return match(p, i, s, j + 1) or match(p, i + 1, s, j + 1)
	elif p[i] == '?':
		return match(p, i + 1, s, j + 1)


import sys

try:
	while True:
		p = sys.stdin.readline().strip()
		s = sys.stdin.readline().strip()
		if not p or not s:
			break
		if match(p, 0, s, 0):
			print 'true'
		else:
			print 'false'
except:
	pass


def solution(pat, match_str):
	m = len(match_str)
	n = len(pat)
	i = 0
	j = 0
	while i < m and j < n:
		if pat[j] not in ['*', '?']:
			if pat[j] == match_str[i]:
				j += 1
				i += 1
			else:
				print '1', 'i', i, 'j', j, pat[j], match_str[i]

				return False
		elif pat[j] == '*':
			print j
			j += 1
			if j < n:
				while j < n and pat[j] in ['*', '?']:
					print pat[j]
					print 'each', j
					j += 1
				while i < m and j < n and pat[j] != match_str[i]:
					i += 1
			else:
				while i < m:
					i += 1
		elif pat[j] == '?':
			j += 1
			i += 1
	if i == m and j == n:
		print '2'
		return True
	return False


# print solution('te?t*.*', 'tett12.xls')
# print solution('te?t*.*', 'txt12.xls')
print solution('nddpv isdc* ?scrg ?g*sg ewtih jlen', 'nddpv isdcb tscrg igssg ewtih jlen')




# import sys
#
# try:
#     while True:
#         pass
# except:
#     pass
