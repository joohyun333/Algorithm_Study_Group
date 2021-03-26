#include <iostream>
#include <map>

int N, L, R;
int A[51][51];
int flood[51][51];
std::map<int, int> PopulationsPerDay;
int ans;

int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { 1, 0, -1, 0 };

void input()
{
	std::cin >> N >> L >> R;
	for (int y = 0; y < N; ++y)
	{
		for (int x = 0; x < N; ++x)
		{
			std::cin >> A[y][x];
		}
	}
}

bool borderCheck(int y, int x, int i)
{
	if (y + dy[i] < 0 || N <= y + dy[i] || x + dx[i] < 0 || N <= x + dx[i])
	{
		return false;
	}
	return true;
}

bool isPossible(int y, int x, int i)
{
	int difference = abs(A[y][x] - A[y + dy[i]][x + dx[i]]);
	if (L <= difference && difference <= R)
	{
		return true;
	}
	return false;
}

void floodFill(int y, int x, int tag, int& cnt, int& sum)
{
	if (flood[y][x] == tag)
	{
		return;
	}
	bool canFill = false;
	
	++cnt;
	sum += A[y][x];

	for (int i = 0; i < 4; ++i)
	{
		if (borderCheck(y, x, i) && isPossible(y, x, i) && flood[y + dy[i]][x + dx[i]] != tag)
		{
			canFill = true;
			flood[y][x] = tag;
			floodFill(y + dy[i], x + dx[i], tag, cnt, sum);
		}
	}
	if (canFill == false && cnt == 1)
	{
		--cnt;
		sum -= A[y][x];
	}
	else if (canFill == false && cnt > 1)
	{
		flood[y][x] = tag;
	}
}

void mergePopulation()
{
	for (int y = 0; y < N; ++y)
	{
		for (int x = 0; x < N; ++x)
		{
			if (flood[y][x] != 0)
			{
				A[y][x] = PopulationsPerDay[flood[y][x]];
				flood[y][x] = 0;
			}
		}
	}
}

void solve()
{
	bool sustainability = false;
	int tag = 1;
	do 
	{
		sustainability = false;
		int cnt = 0;
		int sum = 0;
		for (int y = 0; y < N; ++y)
		{
			for (int x = 0; x < N; ++x)
			{
				if (flood[y][x] == 0)
				{
					floodFill(y, x, tag, cnt, sum);
					if (cnt > 0)
					{
						int avg = sum / cnt;
						PopulationsPerDay[tag] = avg;
						sum = 0;
						cnt = 0;
						++tag;
						sustainability = true;
					}
				}
			}
		}
		mergePopulation();
		++ans;
	} while (sustainability);
	--ans; 
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
