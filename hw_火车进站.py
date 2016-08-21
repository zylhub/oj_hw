import copy
 
def solution(inp, in_, out_):
    if not inp and not in_:
        result.append(' '.join(out_))
    else:
        if in_:
            tmp_inp = copy.copy(inp)
            tmp_in_ = copy.copy(in_)
            tmp_out_ = copy.copy(out_)
            tmp_out_.append(tmp_in_.pop())
            solution(tmp_inp, tmp_in_, tmp_out_)
        if inp:
            tmp_inp = copy.copy(inp)
            tmp_in_ = copy.copy(in_)
            tmp_out_ = copy.copy(out_)
            tmp_in_.append(tmp_inp.pop(0))
            solution(tmp_inp, tmp_in_, tmp_out_)
 
import sys
try:
    while True:
        n = sys.stdin.readline().strip()
        if not n:
            break
        inp = sys.stdin.readline().strip().split()
        in_ = []
        out_ = []
        result = []
        solution(inp, in_, out_)
        result.sort()
        for ret in result:
            print ret
except:
    pass