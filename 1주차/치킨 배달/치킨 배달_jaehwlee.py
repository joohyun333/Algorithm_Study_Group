import sys
from itertools import combinations


def get_distance(ps1, ps2):
  return abs(ps1[0]-ps2[0]) + abs(ps1[1]-ps2[1])


def get_position(city_map):
  house_ps = []
  chicken_ps = []
  for i in range(n):
    for j in range(n):
      if city_map[i][j] == 1:
        house_ps.append((i, j))
      elif city_map[i][j] == 2:
        chicken_ps.append((i, j))
      else:
        continue
  return house_ps, chicken_ps


def solution(house_ps, chicken_ps):
  min_distance = 1e9
  for chicken_candidate in combinations(chicken_ps, m):
    tmp_distance = 0
    for h in house_ps:
      tmp_list = []
      for c in chicken_candidate:
        tmp_distance_list.append(get_distance(h,c))
      tmp_distance += min(tmp_list)
    min_distance = min(min_distance, tmp_distance)
  print(min_distance)

  
input = sys.stdin.readline
n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]
house_ps, chicken_ps = get_position(city_map)
solution(house_ps, chicken_ps)
                        
