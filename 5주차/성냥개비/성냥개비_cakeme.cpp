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

int T, n;
int numOfMatch[9] = {0, 0, 1, 7, 4, 2, 0, 8, 10};
long long dp[101];
int ans;

void input()
{
	std::cin >> T;
}

void calcMinimum()
{
	for (int i = 1; i <= 9; ++i)
	{
		dp[i] = numOfMatch[i];
	}
	dp[6] = 6;
	for (int i = 9; i <= 100; ++i)
	{
		dp[i] = 9223372036854775807i64;
		for (int j = 2; j < 8; ++j)
		{
			dp[i] = min(dp[i], dp[i - j] * 10 + numOfMatch[j]);
		}
	}
}

void solve()
{
	for (int testCase = 0; testCase < T; ++testCase)
	{
		std::cin >> n;
		std::cout << dp[n] << ' ';

		while (n)
		{
			if (n % 2 == 0)
			{
				std::cout << 7;
				n -= 3;
			}
			else
			{
				std::cout << 1;
				n -= 2;
			}
		}
	}
	std::cout << '\n';
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