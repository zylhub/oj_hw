import sys


def set_array_top_right_corner_to_be_zero(inp):
    ret = []
    change_idx = [0, 1, 2, 4, 5, 8]
    for i, val in enumerate(inp):
        if i in change_idx:
            ret.append('0')
        else:
            ret.append(val)
    print ''.join(ret)
try:
    while True:
        line = sys.stdin.readline().strip()
        if line=='':
            break
        inp = []
        inp.append(line)
        for i in range(8):
            n = sys.stdin.readline().strip()
            inp.append(n)
        set_array_top_right_corner_to_be_zero(inp)
        # pass
except:
    pass
