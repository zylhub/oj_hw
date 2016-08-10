# coding=utf-8

# d = {'1': ['1'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
#      '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
#      '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], '0': '0'}

# index2w = {'1': 1, 'a':2, 'b':2, 'c': 2, 'd':3}
index2w = {'1': '1', '0': '0', 'a': '2', 'c': '2', 'b': '2', 'e': '3', 'd': '3', 'g': '4', 'f': '3', 'i': '4',
           'h': '4', 'k': '5', 'j': '5', 'm': '6', 'l': '5', 'o': '6', 'n': '6', 'q': '7', 'p': '7', 's': '7',
           'r': '7', 'u': '8', 't': '8', 'w': '9', 'v': '8', 'y': '9', 'x': '9', 'z': '9'}
# for k, v in d.items():
#     for ch in v:
#         index2w[ch] = k
# print index2w

def solution(inp):
    result = ''
    for ch in inp:
        if '0' <= ch and ch <= '9':
            result += ch
        elif 'a' <= ch and ch <= 'z':
            result += index2w[ch]
        elif 'A' <= ch and ch <= 'Z':
            if ch == 'Z':
                result += 'a'
            else:
                result += chr(ord(ch.lower())+1)
    print result

# solution('YUANzhi1987')

while True:
    try:
        inp = raw_input()
        if inp == '':
            break
        solution(inp)
    except:
        break