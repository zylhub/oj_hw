# coding=utf-8

"""
http://www.nowcoder.com/profile/8481402/codeBookDetail?submissionId=5128409
"""
def solution(seq, n):
    i = 0
    j = 0
    ret = ''
    while i < len(seq) and j < n:
        if not seq[i].isalpha() and j+2 <= n:
            # print 'j', j
            ret += seq[i:i+3]  # python内部一般对汉字3个字节编码
            i += 3
            j += 2
        elif seq[i].isalpha():
            ret += seq[i]
            i += 1
            j += 1
        else: # 汉字取不完，舍弃
            break
    return ret
  
import sys
try:
    while True:
        line = sys.stdin.readline().strip()  # 例子明明是两行输入。。然 实际是一行
        if not line:
            break
        seq, n = line.split()
        # print seq, n
        print solution(seq, int(n))
except:
    pass