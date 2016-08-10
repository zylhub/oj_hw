# coding=utf-8
def solution(inp_lst):
    for e in inp_lst:
        if len(e) < 9:
            print 'NG'
            continue  # 执行下一个循环值
        is_upper, is_lower, is_num, other = 0, 0, 0, 0
        for ch in e:
            if 'A' <= ch and ch <= 'Z':  # 判断是否有大写字母
                is_upper = 1
            elif 'a' <= ch and ch <= 'z':  # 判断是否包含小写
                is_lower = 1
            elif '0' <= ch and ch <= '9':  # 判断是否为数字
                is_num = 1
            else:
                other = 1  # 其他字符
        if is_upper + is_lower + is_num + other < 3:
            print 'NG'
            continue
        result = 'OK'
        for i in range(len(e) - 6):
            if e[i:i + 3] in e[i + 3:]:
                result = 'NG'
                break
        print result


while True:
    try:
        inp_line = raw_input()
        print inp_line
        print inp_line.split()
        solution(inp_line.split())
    except:
        exit(0)
