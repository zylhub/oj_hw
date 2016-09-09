def bisect(nums, val):
    low = 0
    hight = len(nums)-1
    while low <=hight:
        mid = low + (hight-low)//2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            low = mid + 1
        else:
            hight = mid - 1
    return low

def solution(nums):
    end = []
    for val in nums:
        idx = bisect(end,val)
        if len(end)==idx: end.append(val)
        else: end[idx]=val
    return end

import sys
try:
    while True:
        line1 = sys.stdin.readline().strip()
        if not line1:
            break
        for i in range(int(line1)):
            n = sys.stdin.readline().strip()
            nums = sys.stdin.readline().strip()
            nums = map(int, nums.split())
            print solution(nums)
except:
    pass
