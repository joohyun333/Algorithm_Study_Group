def DFS(level, res):
    if level == len(word):
        print(res)
        return
    for i in range(26):
        if alpha[i] == 0:
            continue
        alpha[i] -= 1
        DFS(level+1, res+chr(i+ord('a')))
        # print(res+chr(i+ord('a')))
        alpha[i] += 1

n = int(input())
for _ in range(n):
    word = list(input())
    alpha = [0 for _ in range(26)]
    # 알파벳 개수 세기
    for i in range(len(word)):
        alpha[ord(word[i])-ord('a')] += 1
    DFS(0, "")