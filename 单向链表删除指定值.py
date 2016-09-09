# coding=utf-8
def solution(lst, val):
    if val in lst:
        lst.remove(val)
        return lst
    return None

import sys
try:
    while 1:
        inp = sys.stdin.readline().strip('\n') # 输入只有一行,空格分隔
        if not inp:
            break
        nums = map(int, inp.split())
        # print 'n',nums[0],'head', nums[1], 'del_val', nums[-1]
        lst = [nums[1]]
        i = 2
        while i < nums[0]*2:
            target = nums[i+1]
            idx = lst.index(target)
            lst.insert(idx+1, nums[i])
            i += 2
        print 'lst',lst
        ret = solution(lst, nums[-1])
        print 'ret',ret
        for num in ret:
            print num,

except:
    pass
