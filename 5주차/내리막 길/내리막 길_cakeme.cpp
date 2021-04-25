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

int N, M, H;
int ans;
std::vector<std::vector<int>> mat;
std::vector<std::vector<int>> cache;

int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { 1, 0, -1, 0 };

void input()
{
	std::cin >> M >> N;
	mat.resize(M, std::vector<int>(N));
	cache.resize(M);
	std::fill(cache.begin(), cache.end(), std::vector<int>(N, -1));
	for (int i = 0; i < M; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			std::cin >> mat[i][j];
		}
	}
}

bool border_check(int y, int x)
{
	return (y < 0 || M <= y || x < 0 || N <= x) ? false : true;
}

int bruteforce(int y, int x)
{
	if (y == M - 1 && x == N - 1)
	{
		return 1;
	}

	int& ret = cache[y][x];
	if (ret != -1)
	{
		return ret;
	}

	int sum = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (border_check(y + dy[i], x + dx[i]) && mat[y + dy[i]][x + dx[i]] < mat[y][x])
		{
			sum += bruteforce(y + dy[i], x + dx[i]);
		}
	}

	return ret = sum;
}

void solve()
{
	ans = bruteforce(0, 0);
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