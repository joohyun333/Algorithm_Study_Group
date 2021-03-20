#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <bitset>
#include <unordered_map>

int N, M, ans;
int mat[5][5];
bool chk[5][5];

void input()
{
	std::cin >> N >> M;
	for (int y = 0; y < N; ++y)
	{
		for (int x = 0; x < M; ++x)
		{
			scanf("%1d", &mat[y][x]);
		}
	}
}

bool findCoord(int& y, int& x)
{
	for (int _y = 0; _y < N; ++_y)
	{
		for (int _x = 0; _x < M; ++_x)
		{
			if (!chk[_y][_x])
			{
				y = _y;
				x = _x;
				return true;
			}
		}
	}
	return false;
}

void mark(int axis, int from, int to, bool isRow, bool value)
{
	for (from; from <= to; ++from)
	{
		if (isRow)
		{
			chk[axis][from] = value;
		}
		else
		{
			chk[from][axis] = value;
		}
	}
}

void dfs(int sum)
{
	int y = 0, x = 0;
	if (!findCoord(y, x))
	{
		if (ans < sum)
		{
			ans = sum;
		}
		return;
	}

	// 가로
	int addNum = 0;
	for (int _x = x; _x < M; ++_x, addNum *= 10)
	{
		if (chk[y][_x])
		{
			break;
		}
		mark(y, x, _x, true, true);
		addNum += mat[y][_x];
		dfs(sum + addNum);
		mark(y, x, _x, true, false);
	}
	// 세로
	addNum = mat[y][x] * 10;
	for (int _y = y + 1; _y < N; ++_y, addNum *= 10)
	{
		if (chk[_y][x])
		{
			break;
		}
		mark(x, y, _y, false, true);
		addNum += mat[_y][x];
		dfs(sum + addNum);
		mark(x, y, _y, false, false);
	}

}

void solve()
{
	dfs(0);
}

void output()
{
	std::cout << ans;
}

int main()
{
	input();
	solve();
	output();
	return 0;
}