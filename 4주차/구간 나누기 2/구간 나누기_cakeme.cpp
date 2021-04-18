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

int N, M;
int ans = 987654321;
std::vector<int> vec;

void input()
{
	std::cin >> N >> M;
	vec.resize(N);
	for (int i = 0; i < N; ++i)
	{
		std::cin >> vec[i];
	}
}

bool is_over_split(int highest)
{
	int maximum = vec[0];
	int minimum = vec[0];
	int intervals = 1;
	for (int i = 1; i < vec.size(); ++i)
	{
		maximum = max(vec[i], maximum);
		minimum = min(vec[i], minimum);
		if (highest < maximum - minimum)
		{
			maximum = vec[i];
			minimum = vec[i];
			++intervals;
			if (M < intervals)
			{
				return true;
			}
		}
	}
	return false;
}

void solve()
{
	int high, low;
	high = 10000;
	low = 0;
	while (low <= high)
	{
		int mid = (high + low) / 2;
		if (is_over_split(mid))
		{
			low = mid + 1;
		}
		else
		{
			high = mid - 1;
		}
	}
	ans = low;
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