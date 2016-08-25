def solution(n, nums):
	if n in nums:
		return [n]
	cur_sum = 0
	for i, val in enumerate(nums):
		cur_sum += val
		if cur_sum < n:
			continue
		elif cur_sum > n:
			if n < val:
				return [val] + ['-']+solution(val-n, nums[:i])
			elif n > val:
				return [val] +['+']+ solution(n-val, nums[:i])
		else:
			return nums[i::-1]



import sys
try:
	while True:
		line = sys.stdin.readline().strip()
		if not line:
			break
		nums = [1, 3, 9, 27, 81]
		ret = solution(int(line), nums)
		flag = 1
		d = {-1: '-', 1: '+'}
		result = str(ret[0])
		for i in ret[1:]:
			if i == '-':
				flag *= -1
			elif i=='+':
				flag *= 1
			else:
				result += d[flag] + str(i)
		print result
except:
	pass