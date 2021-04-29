# https://www.acmicpc.net/problem/2602
import sys

input = sys.stdin.readline
key = input().strip()
bridge_of_angel = input().strip()
bridge_of_devil = input().strip()
n = len(bridge_of_angel)

def DP(key_idx, bridge_idx, name):
    bridge_name, DP_name = (bridge_of_angel, DP_angel) if name == "angel" else (bridge_of_devil, DP_devil)
    if bridge_idx >= n:
        return 0
    if DP_name[key_idx][bridge_idx] != -1:
        return DP_name[key_idx][bridge_idx]
    count = 0
    opposite_name = "devil" if name == "angel" else "angel"
    for i in range(bridge_idx, n):
        if bridge_name[i] == key[key_idx]:
            if key_idx == len(key) - 1:
                count += 1
            else:
                # print(key_idx, bridge_idx, DP_name)
                count += DP(key_idx + 1, i + 1, opposite_name)
                DP_name[key_idx][bridge_idx] = count
                # print(key_idx, bridge_idx, DP_name)
    return count

DP_angel = [[-1] * n for _ in range(len(key))]
DP_devil = [[-1] * n for _ in range(len(key))]
a = DP(0, 0, "angel")

DP_angel = [[-1] * n for _ in range(len(key))]
DP_devil = [[-1] * n for _ in range(len(key))]
d = DP(0,0,"devil")
print(a+d)
