#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <bitset>
#include <unordered_map>

struct cctv
{
	int y;
	int x;
	int type;
};

int N, M, ans;
int office[8][8];
std::vector<cctv> cctvs;

int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { 1, 0, -1, 0 };

void input()
{
	std::cin >> N >> M;
	for (int y = 0; y < N; ++y)
	{
		for (int x = 0; x < M; ++x)
		{
			std::cin >> office[y][x];
			if (0 < office[y][x] && office[y][x] < 6)
			{
				cctvs.push_back({ y, x, office[y][x] });
			}
		}
	}
	ans = N * M;
}

int checkEmptySpace()
{
	int sum = 0;
	for (int y = 0; y < N; ++y)
	{
		for (int x = 0; x < M; ++x)
		{
			if (office[y][x] == 0)
			{
				++sum;
			}
		}
	}
	return sum;
}

void checkDirection(int y, int x, int dir, bool isUnCheck)
{
	y += dy[dir];
	x += dx[dir];
	while (0 <= y && y < N && 0 <= x && x < M)
	{
		if (office[y][x] <= 0)
		{
			if (isUnCheck)
			{
				office[y][x] += 1;
			}
			else
			{
				office[y][x] -= 1;
			}
		}
		else if (5 < office[y][x])
		{
			return;
		}
		y += dy[dir];
		x += dx[dir];
	}
}

void typeCheck(int number, int rot, int type, bool isUnCheck)
{
	switch (type)
	{
	case 1:
		checkDirection(cctvs[number].y, cctvs[number].x, (0 + rot) % 4, isUnCheck);
		break;
	case 2:
		checkDirection(cctvs[number].y, cctvs[number].x, (0 + rot) % 4, isUnCheck);
		checkDirection(cctvs[number].y, cctvs[number].x, (2 + rot) % 4, isUnCheck);
		break;
	case 3:
		checkDirection(cctvs[number].y, cctvs[number].x, (0 + rot) % 4, isUnCheck);
		checkDirection(cctvs[number].y, cctvs[number].x, (3 + rot) % 4, isUnCheck);
		break;
	case 4:
		checkDirection(cctvs[number].y, cctvs[number].x, (0 + rot) % 4, isUnCheck);
		checkDirection(cctvs[number].y, cctvs[number].x, (2 + rot) % 4, isUnCheck);
		checkDirection(cctvs[number].y, cctvs[number].x, (3 + rot) % 4, isUnCheck);
		break;
	}
}

void recursiveDFS(int number)
{
	if (number == cctvs.size())
	{
		int emptySpace = checkEmptySpace();
		if (emptySpace < ans)
		{
			ans = emptySpace;
		}
		return;
	}


	if (4 < cctvs[number].type)
	{
		for (int i = 0; i < 4; ++i)
		{
			checkDirection(cctvs[number].y, cctvs[number].x, i, false);
		}
		recursiveDFS(number + 1);
	}
	else
	{
		for (int rot = 0; rot < 4; ++rot)
		{
			typeCheck(number, rot, cctvs[number].type, false);
			recursiveDFS(number + 1);
			typeCheck(number, rot, cctvs[number].type, true);
		}
	}
}

void solve()
{
	recursiveDFS(0);
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