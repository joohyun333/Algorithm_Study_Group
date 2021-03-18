#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <bitset>
#include <unordered_map>

int N, M, ans = 987654321;
int village[52][52];
std::vector<std::pair<int, int>> houses;
std::vector<std::pair<int, int>> chickens;
std::vector<std::vector<int>> mat;
std::vector<int> chickenDists;

void input()
{
	std::cin >> N >> M;
	for (int y = 1; y <= N; ++y)
	{
		for (int x = 1; x <= N; ++x)
		{
			std::cin >> village[y][x];
			if (village[y][x] == 1)
			{
				houses.push_back({ y, x });
			}
			else if (village[y][x] == 2)
			{
				chickens.push_back({ y, x });
			}
		}
	}
}

void solve()
{
	for (auto house : houses)
	{
		mat.push_back(std::vector<int>());
		for (auto chicken : chickens)
		{
			mat.back().push_back({ abs(house.first - chicken.first) + abs(house.second - chicken.second) });
		}
	}
	chickenDists = std::vector<int>(houses.size());

	std::vector<int> permutation(chickens.size());
	for (int i = 0; i < chickens.size(); ++i)
	{
		permutation[i] = i;
	}
	std::vector<int> combination(chickens.size(), 0);
	for (int i = 0; i < M; ++i)
	{
		combination[i] = 1;
	}

	do
	{
		for (int y = 0; y < houses.size(); ++y)
		{
			int minimunDist = 987654321;
			for (int x = 0; x < chickens.size(); ++x)
			{
				if (combination[x] == 0)
				{
					continue;
				}
				if (mat[y][x] < minimunDist)
				{
					minimunDist = mat[y][x];
				}
			}
			chickenDists[y] = minimunDist;
		}
		int sumDist = 0;
		for (auto it : chickenDists)
		{
			sumDist += it;
		}
		ans = sumDist < ans ? sumDist : ans;
	} while (std::prev_permutation(combination.begin(), combination.end()));
}

void output()
{
	std::cout << ans << '\n';
}

int main()
{
	std::cin.tie(0);
	std::cin.sync_with_stdio(false);
	std::cout.tie(0);
	std::cout.sync_with_stdio(false);
	input();
	solve();
	output();
	return 0;
}