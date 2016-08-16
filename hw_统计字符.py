def count_str(inp):
    num = 0
    space = 0
    alpha = 0
    other = 0
    for ch in inp:
        if ch.isdigit():
            num += 1
        elif ch.isspace():
            space += 1
        elif ch.isalpha():
            alpha += 1
        else:
            other += 1
    print alpha
    print space
    print num
    print other

while True:
    try:
        inp = raw_input().strip()
        if inp == '':
            break
        count_str(inp)
    except:
        break