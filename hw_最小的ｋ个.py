import heapq

def get_min_k(lst, k):
    return heapq.nsmallest(k, lst)

import sys

try:
    while 1:
        line = sys.stdin.readline().strip()
        if not line:
            break
        n, k = map(int, line.split())
        lst_inp = sys.stdin.readline().strip()
        lst = map(int, lst_inp.split())
        ret = get_min_k(lst, k)
        for num in ret:
            print num,
        print  #　最后居然要求'\n'

except:
    pass