#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <bitset>
#include <unordered_map>

struct dust
{
	int y;
	int x;
	int amount;
};

int r, c, t, ans;
int room[51][51];
int upper = -1, lower = -1;
std::queue<dust> collectedDust;

int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { 1, 0, -1, 0 };

void input()
{
	std::cin >> r >> c >> t;
	for (int y = 0; y < r; ++y)
	{
		for (int x = 0; x < c; ++x)
		{
			std::cin >> room[y][x];
			if (room[y][x] < 0)
			{
				if (upper == -1)
				{
					upper = y;
				}
				else
				{
					lower = y;
				}
			}
		}
	}
}

bool isIn(int y, int x)
{
	if (0 <= y && y < r && 0 <= x && x < c)
	{
		return true;
	}
	return false;
}

int spread(int fineDust, int y, int x)
{
	int numOfSpread = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (isIn(y + dy[i], x + dx[i]) && 0 <= room[y + dy[i]][x + dx[i]])
		{
			if (0 < fineDust / 5.0f)
			{
				collectedDust.push({ y + dy[i], x + dx[i], (int)(fineDust / 5.0f) });
			}
			++numOfSpread;
		}
	}
	return numOfSpread;
}

void update()
{
	for (int y = 0; y < r; ++y)
	{
		for (int x = 0; x < c; ++x)
		{
			if (0 < room[y][x])
			{
				collectedDust.push({ y, x, room[y][x] });
			}
		}
	}

	int numOfDust = collectedDust.size();
	for (int iter = 0; iter < numOfDust; ++iter)
	{
		dust current = collectedDust.front();
		collectedDust.pop();
		int numOfSpread = spread(current.amount, current.y, current.x);
		room[current.y][current.x] -= (int)(current.amount / 5.0f) * numOfSpread;
	}

	numOfDust = collectedDust.size();
	for (int iter = 0; iter < numOfDust; ++iter)
	{
		dust current = collectedDust.front();
		collectedDust.pop();
		room[current.y][current.x] += current.amount;
	}
}

void operateAirPurifier()
{
	// trash code
	for (int y = upper - 1; 0 < y; --y)
	{
		room[y][0] = room[y - 1][0];
	}
	for (int x = 0; x < c - 1; ++x)
	{
		room[0][x] = room[0][x + 1];
	}
	for (int y = 0; y < upper; ++y)
	{
		room[y][c - 1] = room[y + 1][c - 1];
	}
	for (int x = c - 1; 1 < x; --x)
	{
		room[upper][x] = room[upper][x - 1];
	}
	room[upper][1] = 0;

	for (int y = lower + 1; y < r - 1; ++y)
	{
		room[y][0] = room[y + 1][0];
	}
	for (int x = 0; x < c - 1; ++x)
	{
		room[r - 1][x] = room[r - 1][x + 1];
	}
	for (int y = r - 1; lower < y; --y)
	{
		room[y][c - 1] = room[y - 1][c - 1];
	}
	for (int x = c - 1; 1 < x; --x)
	{
		room[lower][x] = room[lower][x - 1];
	}
	room[lower][1] = 0;
}

void solve()
{
	for (int time = 0; time < t; ++time)
	{
		update();
		operateAirPurifier();
	}
}

void output()
{
	for (int y = 0; y < r; ++y)
	{
		for (int x = 0; x < c; ++x)
		{
			if (0 < room[y][x])
			{
				ans += room[y][x];
			}
		}
	}
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
