def solution(sentence, keyword, skips):
    basic = sentence
    n_skips = [skips[0]]
    total_len = len(sentence)+1
    for i in range(1, len(skips)):
        n = n_skips[-1] + skips[i] + 1
        if n <= total_len:
            n_skips.append(n)
        else:
            if sentence[-1] == keyword[i%len(keyword)]:
                n_skips.append(n)
            break
        total_len += 1

    for i in range(len(n_skips)):
        n = sentence[0:n_skips[i]] + keyword[i % len(keyword)] + sentence[n_skips[i]:]
        sentence = n

    arr = [n_skips[0]]
    keyword_idx = 1
    for i in range(1, len(n_skips)):
        count = n_skips[i]
        for j in range(n_skips[i - 1] + 1, n_skips[i]):
            if sentence[j] == keyword[keyword_idx % len(keyword)]:
                count = j
                keyword_idx+=1
                break
        arr.append(count)
        keyword_idx += 1
    for i in range(len(arr)):
        n = basic[0:arr[i]] + keyword[i % len(keyword)] + basic[arr[i]:]
        basic = n

    return basic


sentence = "i love coding"
keyword = "mask"
skips = [0, 0, 3, 2, 3, 4]
#mai lsovke cmodinag

sentence = "i love coding"
keyword = "mode"
skips = [0, 10]
#mi loove coding

sentence ="abcde fghi"
keyword ="xyz"
skips =[10,0,1]
#abcde fghixy

sentence ="encrypt this sentence"
keyword ="something"
skips =[0,1,3,2,1,2,0,3,0,2,4,1,3]
#seoncrmypett thihisng ssenteonmcee

sentence ="bbbbb"
keyword ="aaaa"
skips =[2,3,1]
#bbabbba
print(solution(sentence, keyword, skips))
