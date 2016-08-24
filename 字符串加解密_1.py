d_en = {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'}
d_word = {'z': 'A', 'Z': 'a'}
d_word_un = {'A': 'z', 'a': 'Z'}
d_unen = {'1': '0', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '0': '9', '9':'8'}


def encrypt(line):
	ret = ''
	for ch in line:
		if ch.isalpha():
			if ch in ['Z', 'z']:
				ret += d_word[ch]
			else:
				ret += chr(ord(ch) + 1).swapcase()
		elif ch.isdigit():
			ret += d_en[ch]
		else:
			ret += ch

	return ret


def unencrypt(line):
	# print line
	ret = []
	for ch in line:
		if ch.isalpha():
			if ch in ['a', 'A']:
				ret.append(d_word_un[ch])
			else:
				ret.append(chr(ord(ch) - 1).swapcase())
		elif ch.isdigit():
			ret.append(d_unen[ch])
		else:
			ret.append(ch)
		# print 'ret', ret
	return ''.join(ret)


import sys

try:
	while True:
		line1 = sys.stdin.readline().strip()
		if not line1:
			break
		line2 = sys.stdin.readline().strip()
		print encrypt(line1)
		print unencrypt(line2)
except:
	pass
