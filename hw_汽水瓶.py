def solution(n):
    count = 0
    while n > 1:
        count += n/3
        n = n/3 + n%3
        if n==2:
            count += 1
            return count
    return count

# print solution(10)
while True:
    try:
        n = input()
        if n=='':
            break
        print solution(n)

    except:
        exit(0)
