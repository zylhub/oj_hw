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
