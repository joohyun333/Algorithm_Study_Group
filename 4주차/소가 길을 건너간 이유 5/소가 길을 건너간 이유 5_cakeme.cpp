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

int N, K, B;
int ans;

bool crosswalk[100010];

constexpr int min(int first, int second)
{
	return first < second ? first : second;
}

void input()
{
	std::cin >> N >> K >> B;
	for (int i = 0; i < B; ++i)
	{
		int in;
		std::cin >> in;
		crosswalk[in] = true;
	}
}

void solve()
{
	int minLight = B;
	int cnt = 0;
	for (int i = 1; i <= K; ++i)
	{
		if (crosswalk[i])
		{
			++cnt;
		}
	}
	minLight = min(minLight, cnt);
	for (int i = K + 1; i <= N; ++i)
	{
		if (crosswalk[i - K])
		{
			--cnt;
		}
		if (crosswalk[i])
		{
			++cnt;
		}
		minLight = min(minLight, cnt);
	}
	ans = minLight;
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