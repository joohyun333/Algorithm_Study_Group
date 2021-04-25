#include <iostream>
#include <algorithm>
/*
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
*/
struct wire
{
	int A;
	int B;
};

wire arr[101];
int dp[101];

bool cmp(wire& first, wire& second)
{
	if (first.A < second.A)
		return true;
	else
		return false;
}

int main()
{
	int N;
	std::cin >> N;
	for (int i = 0; i < N; ++i)
	{
		std::cin >> arr[i].A >> arr[i].B;
	}
	std::sort(arr, arr + N, cmp);
	
	int back = 0;
	for (int i = 0; i < N; ++i)
	{
		int it = 0;
		for( ;dp[it] != 0; ++it)
		{
			if (dp[it] > arr[i].B)
			{
				dp[it] = arr[i].B;
				break;
			}
		}
		dp[it] = arr[i].B;
		back = back > it ? back : it;
	}
	std::cout << N - (back + 1);
	return 0;
}

/*
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

int n;
int ans;
std::vector<int> cache, poles;

struct wire
{
	int A;
	int B;
};

wire arr[101];
int dp[101];

bool cmp(wire& first, wire& second)
{
	if (first.A < second.A)
		return true;
	else
		return false;
}


void input()
{
	std::cin >> n;
	for (int i = 0; i < n; ++i)
	{
		std::cin >> arr[i].A >> arr[i].B;
	}
	std::sort(arr, arr + n, cmp);
}

void solve()
{
	int back = 0;
	for (int i = 0; i < n; ++i)
	{
		int it = 0;
		for (; dp[it] != 0; ++it)
		{
			if (dp[it] > arr[i].B)
			{
				dp[it] = arr[i].B;
				break;
			}
		}
		dp[it] = arr[i].B;
		back = back > it ? back : it;
	}
	ans = n - (back + 1);
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
*/