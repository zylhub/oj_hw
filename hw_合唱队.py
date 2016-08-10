# coding=utf-8
"""
1 ti_1<ti>Ti+1
"""


# def solution(inp_str, n):
#     left = [1 for i in range(n)]
#     right = [1 for i in range(n)]
#     gen_a = (max(left[i], left[j]+1) for i in range(1,n) for j in range(i) if inp_str[i] > inp_str[j])
#     gen_b = (max(right[i], right[j]+1) for i in range(n-2,-1,-1) for j in range(n-1,i,-1) if inp_str[i] > inp_str[j])
#     i=1
#     for a, b in zip(gen_a, gen_b):
#         print a, b
#         left[i] = a
#         right[i] = b
#         i += 1
#
#     cout = 0
#     for i in range(n):
#         cout = max(cout, left[i]+right[i]-1)
#         # print cout
#     return n-cout


def solution(inp_str, n):
    left = [1]*n
    right = [1]*n
    for i in range(1,n):
        tmp_i = inp_str[i]
        for j in range(i):
            tmp = left[j] + 1
            if tmp_i > inp_str[j] and left[i] < tmp:
                left[i] = tmp
    for i in range(n-2,-1,-1):
        tmp_i = inp_str[i]
        for j in range(n-1,i,-1):
            tmp = right[j] + 1
            if tmp_i > inp_str[j] and right[i] < tmp:
                right[i] = tmp

    cout = 0
    for i in range(n):
        cout = max(cout, left[i]+right[i]-1)
    return n-cout
from time import time

while True:
    try:
        n = input()
        if n=='':
            break
        inp = raw_input()
        inp_str = map(int, inp.split())
        t = time()
        print solution(inp_str, n)
        print time()-t
    except:
        break

# def solution(inp_str, n):
#     if n < 3:
#         return
#
#     count = 0
#     for i in range(n):
#         current = inp_str[i]
#         left = 0
#         right = 0
#         for left_num in inp_str[i::-1]:
#             if left_num < current:
#                 left += 1
#                 current = left_num
#
#         current = inp_str[i]
#         for right_num in inp_str[i:]:
#             if right_num < current:
#                 right += 1
#                 current = right_num
#
#         print 'i',i,left, right
#         tmp = left + right + 1
#         if tmp > count:
#             count = tmp
#
#
#     return n-count



