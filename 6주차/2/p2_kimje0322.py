def end(sen):
    answer = ''
    for s in sen:
        answer += s
    return answer

def solution(sentence, keyword, skips):
    sentence = list(sentence)
    cur_idx = 0
    # skips 인덱스
    for s_idx in range(len(skips)):
        overlap = False
        # 키워드 인덱스
        key_idx = s_idx % len(keyword)
        # 넣을 위치 인덱스
        target_idx = cur_idx + skips[s_idx]

        # 4번 예외케이스
        # 넣어야할 인덱스가 sentence인덱스 넘어가면
        if target_idx > len(sentence):
            # 마지막 요소와 같으면 append -> return
            if sentence[-1] == keyword[key_idx]:
                sentence.append(keyword[key_idx])
            # 다르면 바로 return
            return end(sentence)

        # 범위 내에서 겹치는 글자 있는지 확인
        idx = cur_idx
        while 0 < idx < target_idx:
            if sentence[idx] == keyword[key_idx]:
                overlap = True
                sentence.insert(idx + 1, keyword[key_idx])
                cur_idx = idx + 2
                break
            idx += 1

        # 겹치지 않으면
        if not overlap:
            sentence.insert(target_idx, keyword[key_idx])
            cur_idx = target_idx + 1

    return end(sentence)



# print(solution("i love coding", "mask", [0, 0, 3, 2, 3, 4]))
# print(solution("i love coding", "mode", [0, 10]))
# print(solution("abcde fghi", "xyz", [10, 0, 1]))
# print(solution("encrypt this sentence", "something", [0, 1, 3, 2, 1, 2, 0, 3, 0, 2, 4, 1, 3]))
# seoncrmypett thihisng ssenteonmcee
print(solution("i loove coding", "mode", [0, 3, 5, 10]))
# sentence = "i loove coding"
# keyword = "mode",
# skips = [0, 3, 5, 10]