#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <bitset>
#include <unordered_map>

int N, maxN = 1000000001;
std::vector<int> K;
int ans;

void input()
{
	int KSize;
	std::cin >> N >> KSize;
	K = std::vector<int>(KSize);
	for (int i = 0; i < KSize; ++i)
	{
		std::cin >> K[i];
	}
}

void dfs(int sum)
{
	if (sum > ans)
	{
		ans = sum;
	}
	for (auto iter : K)
	{
		if (maxN > sum && N >= sum * 10 + iter)
		{
			dfs(sum * 10 + iter);
		}
	}
}

void solve()
{
	dfs(0);
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