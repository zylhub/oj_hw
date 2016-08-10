from itertools import permutations


def is_stack(inp, out, n):
    s = []
    j = 0
    for i in range(n):
        s.append(inp[i])
        while s != [] and s[-1] == out[j]:
            s.pop()
            j += 1
    if s == []:
        return True
    else:
        return False


# def solution(inp_str, n):
#     tmp = []
#     inp = map(int, inp_str)
#     for e in permutations(inp, n):
#         tmp.append(e)
#     inp = map(int, inp)
#     tmp = [e for e in tmp if is_stack(inp, e, n)]
#     tmp.sort()
#     for e in tmp:
#         print ' '.join(map(str, e))

def solution(inp_str, n):
    for e in permutations(range(1,n+1), n):
        if is_stack(inp_str, e, n):
            print ' '.join(map(str, e))
    # tmp = (e for e in permutations(start, n) if is_stack(inp, e, n))
    # for e in tmp:
    #     print ' '.join(map(str, e))


solution([6,1,5,3,2,7,4],7)

# import sys
#
# try:
#     while True:
#         line_1 = sys.stdin.readline().strip()
#
#         # print line_2, line_1
#         if line_1 == '':
#             break
#         line_2 = sys.stdin.readline().strip()
#         n = int(line_1)
#         inp_str = line_2.split()
#         solution(inp_str, n)
#
# except:
#     pass
