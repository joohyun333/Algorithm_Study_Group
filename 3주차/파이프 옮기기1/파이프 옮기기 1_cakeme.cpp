#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <map>
#include <unordered_map>

int r, c, N, ans;
int mat[20][20];

void input()
{
	std::cin >> N;
	for (int y = 1; y <= N; ++y)
	{
		for (int x = 1; x <= N; ++x)
		{
			std::cin >> mat[y][x];
		}
	}
}

/*
* 가로 : 1
* 대각선 : 2
* 세로 : 3
*/

void dfs(int y, int x, int state)
{
	if (y == N && x == N)
	{
		++ans;
		return;
	}

	if (x + 1 <= N && state != 3 && mat[y][x + 1] != 1)
	{
		dfs(y, x + 1, 1);
	}
	if (y + 1 <= N && x + 1 <= N && mat[y + 1][x] != 1 && mat[y + 1][x + 1] != 1 && mat[y][x + 1] != 1)
	{
		dfs(y + 1, x + 1, 2);
	}
	if (y + 1 <= N && state != 1 && mat[y + 1][x] != 1)
	{
		dfs(y + 1, x, 3);
	}
}

void solve()
{
	dfs(1, 2, 1);
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