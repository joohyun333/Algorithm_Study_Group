def end(sen):
    answer = ''
    for s in sen:
        answer += s
    return answer


def solution(sentence, keyword, skips):
    sentence = list(sentence)
    cur_idx = 0
    for s_idx in range(len(skips)):
        key_idx = s_idx % len(keyword)
        overlap = False
        target_idx = cur_idx + skips[s_idx]
        idx = cur_idx

        if target_idx > len(sentence):
            if sentence[-1] == keyword[key_idx]:
                sentence.append(keyword[key_idx])
            return end(sentence)

        while 0 < idx < target_idx:
            if sentence[idx] == keyword[key_idx]:
                overlap = True
                sentence.insert(idx + 1, keyword[key_idx])
                cur_idx = idx + 2
                break
            idx += 1
        if not overlap:
            sentence.insert(target_idx, keyword[key_idx])
            cur_idx = target_idx + 1

    return end(sentence)


# seoncrmypett thihisng ssenteonmcee
print(solution("i love coding", "mask", [0, 0, 3, 2, 3, 4]))
print(solution("i love coding", "mode", [0, 10]))
print(solution("abcde fghi", "xyz", [10, 0, 1]))
print(solution("encrypt this sentence", "something", [0, 1, 3, 2, 1, 2, 0, 3, 0, 2, 4, 1, 3]))
# SeOncrMypEtT tHIhisNG sSenteOnMceE
