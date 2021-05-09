#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <vector>
#include <array>
#include <map>
#include <set>
#include <unordered_map>
#include <cmath>

constexpr int min(int first, int second)
{
	return first < second ? first : second;
}

constexpr int max(int first, int second)
{
	return first < second ? second : first;
}

int ans;
std::string scroll, angel, devil;
std::vector<int> cache[2];

void input()
{
	std::cin >> scroll >> devil >> angel;
}

int bruteforce(std::string& bridge, int index, int order)
{
	if (scroll.size() <= order)
	{
		return 1;
	}
	if (bridge.size() <= index)
	{
		return 0;
	}

	int sum = 0;
	for (int i = index; i < bridge.size(); ++i)
	{
		if (bridge[i] == scroll[order])
		{
			int& ret = &bridge == &angel ? cache[1][i] : cache[0][i];
			if (ret != -1)
			{
				return ret;
			}
			ret = 0;

			std::string& another = &bridge == &angel ? devil : angel;
			ret += bruteforce(another, i + 1, order + 1);
			sum += ret;
		}
	}
	return sum;
}

void solve()
{
	int sum = 0;
	cache[0].resize(devil.size(), -1);
	cache[1].resize(angel.size(), -1);
	sum += bruteforce(devil, 0, 0);

	std::fill(cache[0].begin(), cache[0].end(), -1);
	std::fill(cache[1].begin(), cache[1].end(), -1);
	sum += bruteforce(angel, 0, 0);

	ans = sum;
}

void output()
{
	std::cout << ans;
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