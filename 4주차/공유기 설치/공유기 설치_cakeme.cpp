#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <map>
#include <set>
#include <unordered_map>

int N, C;
int ans;

std::vector<int> vec;

void input()
{
	std::cin >> N >> C;
	vec = std::vector<int>(N);
	for (int i = 0; i < N; ++i)
	{
		std::cin >> vec[i];
	}
	std::sort(vec.begin(), vec.end());
}

bool IsPossible(int dist)
{
	int prevPos = vec.front();
	int cnt = 0;
	for (int i = 1; i < N - 1; ++i)
	{
		if (vec.back() - vec[i] < dist)
		{
			break;
		}
		if (dist <= vec[i] - prevPos)
		{
			prevPos = vec[i];
			++cnt;
			if (C - 2 <= cnt)
			{
				return true;
			}
		}
	}
	return false;
}

void solve()
{
	int median = (vec.back() - vec.front()) / C;
	std::map<int, bool> dists;
	int upper, lower;
	upper = vec.back() - vec.front();
	lower = 1;
	while (true)
	{
		bool possibility = IsPossible(median);
		if (dists.find(median) == dists.end())
		{
			dists[median] = possibility;
		}
		else
		{
			break;
		}
		if (possibility)
		{
			lower = median;
			median = (upper - median) / 2 + median;
		}
		else
		{
			upper = median;
			median = (median - lower) / 2 + lower;
		}
	}
	ans = median;
	return;
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