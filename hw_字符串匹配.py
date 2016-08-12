def all_char_exist(short_str, long_str):
    short_str = set(list(short_str))
    long_str = set(list(long_str))
    for ch in short_str:
        if ch not in long_str:
            return False
    return True

import sys

try:
    while True:
        short_str = sys.stdin.readline().strip()
        long_str = sys.stdin.readline().strip()
        if not short_str or not long_str:
            raise ValueError
        if all_char_exist(short_str, long_str):
            print 'true'
        else:
            print 'false'
except:
    pass