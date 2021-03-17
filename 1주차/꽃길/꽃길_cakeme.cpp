///////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <bitset>
#include <unordered_map>

int N, ans = 987654321;
int ground[10][10];
bool purchased[10][10];

int dy[5] = { 1, 0, -1, 0, 0 };
int dx[5] = { 0, 1, 0, -1, 0 };

struct coord
{
	int y;
	int x;
};

void input()
{
	std::cin >> N;
	for (int y = 0; y < N; ++y)
	{
		for (int x = 0; x < N; ++x)
		{
			std::cin >> ground[y][x];
		}
	}
}

bool canBlossom(int y, int x)
{
	if (y <= 0 || N - 1 <= y || x <= 0 || N - 1 <= x)
	{
		return false;
	}

	for (int i = 0; i < 5; ++i)
	{
		if (purchased[y + dy[i]][x + dx[i]])
		{
			return false;
		}
	}
	return true;
}

int setGround(int y, int x, bool isPurchase)
{
	int chargeCount = 0;
	for (int i = 0; i < 5; ++i)
	{
		chargeCount += ground[y + dy[i]][x + dx[i]];
		purchased[y + dy[i]][x + dx[i]] = isPurchase;
	}
	return chargeCount;
}

void plantSeeds(int seedIdx, int charge, coord seedPosition)
{
	if (seedIdx >= 3)
	{
		if (charge < ans)
		{
			ans = charge;
		}
		return;
	}

	for (int y = seedPosition.y; y < N - 1; ++y)
	{
		for (int x = 1; x < N - 1; ++x)
		{
			if (canBlossom(y, x))
			{
				int currCharge = setGround(y, x, true);
				plantSeeds(seedIdx + 1, charge + currCharge, { y, x + 1 });
				setGround(y, x, false);
			}
		}
	}
}

void solve()
{
	plantSeeds(0, 0, { 0, 0 });
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