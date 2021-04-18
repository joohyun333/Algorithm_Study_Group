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

int N;
std::pair<int, int> ans;
std::vector<int> vec;

constexpr int min(int first, int second)
{
	return first < second ? first : second;
}

constexpr int max(int first, int second)
{
	return first < second ? second : first;
}

void input()
{
	std::cin >> N;
	vec.resize(N);
	for (int i = 0; i < N; ++i)
	{
		std::cin >> vec[i];
	}
	std::sort(vec.begin(), vec.end());
}

int get_close_num(int num, int index)
{
	int absNum = abs(num);
	int upper = vec.size() - 1;
	int lower = index + 1;
	int median = (upper - lower) / 2 + lower;
	int comparison = median;
	while (true)
	{
		if (upper <= lower || vec[median] + num == 0)
		{
			return vec[comparison];
		}
		if (vec[median] + num < 0)
		{
			lower = median + 1;
		}
		else
		{
			upper = median - 1;
		}
		median = (upper - lower) / 2 + lower;
		comparison = abs(vec[median] + num) < abs(vec[comparison] + num) ? median : comparison;
	}
	return vec[comparison];
}

void solve()
{

	int lowest = 2000000000;
	for (int i = 0; i < N - 1; ++i)
	{
		int first = vec[i];
		int second = get_close_num(first, i);
		if (abs(first + second) < lowest)
		{
			lowest = abs(first + second);
			ans.first = first;
			ans.second = second;
		}
	}
}

void output()
{
	std::cout << ans.first << ' ' << ans.second << '\n';
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