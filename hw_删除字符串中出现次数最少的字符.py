# coding = utf-8

# solution 1, use build-in collections
# http://www.nowcoder.com/practice/05182d328eb848dda7fdd5e029a56da9?tpId=37&tqId=21246&rp=&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking
while True:
    try:
        input_text = raw_input()
        if input_text == '\n':
            break
        from collections import Counter

        counter = Counter(input_text)
        value = counter.most_common()[-1][1]
        for ch, val in counter.most_common():
            if val == value:
                input_text = input_text.replace(ch, '')
        print input_text
    except:
        break

# solution 2
def solution(inp_str):
    ch_set = set(inp_str)
    min_count = 21
    for ch in ch_set:
        ch_count = inp_str.count(ch)
        if ch_count < min_count:
            min_count = ch_count
    ret = ''
    for e in inp_str:
        if inp_str.count(e)==min_count:
            continue
        else:
            ret += e
    return ret

while True:
    try:
        inp = raw_input()
        if inp == '':
            break
        print solution(inp)
    except:
        exit(0)

print solution('abcdd')