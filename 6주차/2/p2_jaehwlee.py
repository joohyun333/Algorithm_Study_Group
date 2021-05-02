case1 = {
    "sentence" : "i love coding",
    "keyword" : "mask",
    "skips" : [0, 0, 3, 2, 3, 4],
}


case2 = {
    "sentence" : "i love coding",
    "keyword" : "mode",
    "skips" : [0, 10],
}


case3 = {
    "sentence": "abcde fghi",
    "keyword" : "xyz",
    "skips" : [10, 0, 1],
}

case4 = {
    "sentence" : "encrypt this sentence",
    "keyword" : "something",
    "skips" : [0, 1, 3, 2, 1, 2, 0, 3, 0, 2, 4, 1, 3],
}

case5 = {
    "sentence" : "bbbbb",
    "keyword" : "aaaa",
    "skips" : [2, 3, 1]
}

# mi looove dcoding
case6 = {
    "sentence" : "i loove coding",
    "keyword" : "mode",
    "skips" : [0, 3, 5, 10]
}

from collections import deque

def solution(sentence, keyword, skips):
  remain = deque(sentence)
  answer = ""
  
  for i, skip in enumerate(skips):
    p = 0

    while p != skip:
      if remain:
        if remain[0] == keyword[i%len(keyword)]:
          answer += remain.popleft()
          break

        answer += remain.popleft()
        p += 1

      else:
        return answer

    answer += keyword[i%len(keyword)]
    
  if len(remain) > 0:
    while len(remain) >0:
      answer += remain.popleft()
  return answer

print(solution(case1["sentence"], case1["keyword"], case1["skips"]))
print(solution(case2["sentence"], case2["keyword"], case2["skips"]))
print(solution(case3["sentence"], case3["keyword"], case3["skips"]))
print(solution(case4["sentence"], case4["keyword"], case4["skips"]))
print(solution(case5["sentence"], case5["keyword"], case5["skips"]))
print(solution(case6["sentence"], case6["keyword"], case6["skips"]))
