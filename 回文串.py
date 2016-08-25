# coding=utf-8

"""
给定一个字符串，问是否能通过添加一个字母将其变为回文串。
http://www.nowcoder.com/profile/8481402/codeBookDetail?submissionId=5461229
"""
def solution(inp):
    """
    添加使得构成回文，那么说明添加之前有一个字符使得不是回文，删除该字符后
    应该构成回文
    """
    if not inp or len(inp)<=2:
        return True
    for i in range(len(inp)):
        tmp = inp[:i] + inp[i+1:]
        if tmp[::-1] == tmp:
            return True
    return False

import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        if solution(line):
            print 'YES'
        else:
            print 'NO'
except:
    pass