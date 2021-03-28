#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <map>
#include <unordered_map>

// 30분 정도? 걸림

int R, C;
char map[11][11];
bool chk[11][11];
std::queue<std::pair<int, int>> islandCoord;
int top, bottom, left, right;

int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { 1, 0, -1, 0 };

void input()
{
	std::cin >> R >> C;
	bottom = R;
	right = C;
	for (int y = 0; y < R; ++y)
	{
		for (int x = 0; x < C; ++x)
		{
			std::cin >> map[y][x];
			if (map[y][x] == 'X')
			{
				islandCoord.push({ y, x });
			}
		}
	}
}

bool borderCheck(int y, int x)
{
	if (y < 0 || R <= y || x < 0 || C <= x)
	{
		return false;
	}
	return true;
}

bool coastCheck(int y, int x)
{
	int cnt = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (borderCheck(y + dy[i], x + dx[i]) == false || map[y + dy[i]][x + dx[i]] == '.')
		{
			++cnt;
		}
	}
	if (3 <= cnt)
	{
		return true;
	}
	else
	{
		return false;
	}
}

void solve()
{
	while (!islandCoord.empty())
	{
		std::pair<int, int> currCoord = islandCoord.front();
		islandCoord.pop();
		if (coastCheck(currCoord.first, currCoord.second))
		{
			chk[currCoord.first][currCoord.second] = true;
		}
	}
	for (int y = 0; y < R; ++y)
	{
		for (int x = 0; x < C; ++x)
		{
			if (chk[y][x] == true)
			{
				map[y][x] = '.';
			}
		}
	}
}

void updateTop(int y, int x)
{
	static bool isUpdated = false;
	if (isUpdated == false)
	{
		if (map[y][x] == 'X')
		{
			top = y;
			isUpdated = true;
		}
	}
}

void updateLeft(int y, int x)
{
	static bool isUpdated = false;
	if (isUpdated == false)
	{
		if (map[y][x] == 'X')
		{
			left = x;
			isUpdated = true;
		}
	}
}

void output()
{
	for (int y = 0; y < R; ++y)
	{
		for (int x = 0; x < C; ++x)
		{
			updateTop(y, x);

			if (map[y][x] == 'X')
			{
				bottom = y;
			}
		}
	}

	for (int x = 0; x < C; ++x)
	{
		for (int y = 0; y < R; ++y)
		{
			updateLeft(y, x);

			if (map[y][x] == 'X')
			{
				right = x;
			}
		}
	}

	for (int y = top; y <= bottom; ++y)
	{
		for (int x = left; x <= right; ++x)
		{
			std::cout << map[y][x];
		}
		std::cout << '\n';
	}
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