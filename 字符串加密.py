d_num = {'0':'1','1':'2', '2':'3', '3':'4', '4': '5', '5': '6', '6': '7', '7': '8', '8':'9', '9':'0'}
reverse_d_num = { v:k for k, v in d_num.items()}

def convert_alpha(ch):
    if ch not in ['z', 'Z']:
        return chr(ord(ch)+1).swapcase()
    elif ch=='z':
        return 'A'
    elif ch=='Z':
        return 'a'
    else:
        return ch

def reverse_alpha(ch):
    if ch not in ['A', 'a']:
        return chr(ord(ch)-1).swapcase()
    elif ch=='A':
        return 'z'
    elif ch=='a':
        return 'Z'
    else:
        return ch

def encrypt(inp_str, d_dict, convert_fun):
    result = ''
    for ch in inp_str:
        if ch.isdigit():
            result += d_dict[ch]
        else:
            result += convert_fun(ch)
    print result

while True:
    try:
        inp_en = raw_input()
        if inp_en == '':
            break
        inp_un = raw_input()
        # print inp_en
        encrypt(inp_en, d_num, convert_alpha)
        encrypt(inp_un, reverse_d_num, reverse_alpha)
    except:
        break