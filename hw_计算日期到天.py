# coding=utf-8
"""
http://www.nowcoder.com/profile/8481402/codeBookDetail?submissionId=4803369
实际输入应该是 年 月 日 在一行用空格分割
"""

d_count = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243,
           10: 273, 11: 304, 12: 334}
month_valid = range(1, 13)
day_valid = range(1, 32)


def is_leap_year(year):
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		return True
	else:
		return False


def convert_date_to_day(year, month, day):
	# print "###enter=="
	if year < 0:
		return -1
	elif month not in month_valid:
		return -1
	elif day not in day_valid:
		return -1

	if month == 1:
		return day
	elif month == 2:
		if day < 29:
			return d_count[2] + day
		elif day == 29 and is_leap_year(year):
			return d_count[2] + day
		else:
			return -1
	else:
		if is_leap_year(year):
			return d_count[month] + day + 1
		else:
			return d_count[month] + day
			# print "####"


while True:
	try:
		inp = raw_input().strip()
		if not inp:
			break
		year, month, day = map(int, inp.split())
		print convert_date_to_day(year, month, day)
	except:
		break
