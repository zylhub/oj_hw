# coding=utf-8
def bubble_count(lst, n):
    """
    题意应该是只能交换相邻数字，冒泡排序是一种交换排序，统计交换次数即可
    http://www.nowcoder.com/profile/8481402/test/4437133/44583#summary
    """
    swap_count = 0
    for i in range(n):
        for j in range(1,n-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                swap_count += 1
    return swap_count


import sys

try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        n = int(line)
        nums = map(int, sys.stdin.readline().strip().split())
        print bubble_count(nums, n)
except:
    pass