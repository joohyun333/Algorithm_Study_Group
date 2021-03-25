#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <bitset>
#include <unordered_map>

struct coord
{
	int y;
	int x;
};

int N;
std::vector<std::string> mat;
std::string ans;

int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { 1, 0, -1, 0 };

void input()
{
	std::cin >> N;
	mat = std::vector<std::string>(N);
	for (int y = 0; y < N; ++y)
	{
		std::cin >> mat[y];
	}
}

bool isMixed(int _y, int _x, int height, int width)
{
	char dot = mat[_y][_x];
	for (int y = _y; y < height; ++y)
	{
		for (int x = _x; x < width; ++x)
		{
			if (mat[y][x] != dot)
			{
				return true;
			}
		}
	}
	return false;
}

void quadtree(coord TopLeft, coord TopRight, coord BottomLeft, coord BottomRight)
{
	if (!isMixed(TopLeft.y, TopLeft.x, BottomRight.y, BottomRight.x))
	{
		ans += mat[TopLeft.y][TopLeft.x];
		return;
	}

	coord center = { (BottomLeft.y + TopLeft.y) / 2.0f, (TopRight.x + TopLeft.x) / 2.0f };
	ans += '(';
	quadtree(TopLeft, { TopLeft.y, center.x }, { center.y, TopLeft.x }, center);
	quadtree({ TopLeft.y, center.x }, TopRight, center, { center.y, TopRight.x });
	quadtree({ center.y, TopLeft.x }, center, BottomLeft, { BottomLeft.y, center.x });
	quadtree(center, { center.y, TopRight.x }, { BottomLeft.y, center.x }, BottomRight);
	ans += ')';
}

void solve()
{
	coord TopLeft = { 0, 0 };
	coord TopRight = { 0, N };
	coord BottomLeft = { N, 0 };
	coord BottomRight = { N, N };
	quadtree(TopLeft, TopRight, BottomLeft, BottomRight);
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