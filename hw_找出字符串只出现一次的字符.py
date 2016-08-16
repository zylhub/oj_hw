def find_char(inp_str):
    n = len(inp_str)
    if n==1:
        return inp_str
    for i in range(n-1):
        if inp_str[i] not in inp_str[:i] and inp_str[i] not in inp_str[i+1:]:
            return inp_str[i]
    if inp_str[-1] not in inp_str[:-1]:
        return inp_str[-1]
    return '.'

def find_char_2(inp_str):
    for ch in inp_str:
        if inp_str.count(ch)==1:
            return ch
    return '.'

import sys

try:
    while True:
        inp_str = sys.stdin.readline().strip()
        if not inp_str:
            raise ValueError
        print find_char(inp_str)
except:
    pass