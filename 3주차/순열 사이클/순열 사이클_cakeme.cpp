#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <map>
#include <unordered_map>

int T, ans;
std::vector<int> vec;
std::vector<int> check;

void input()
{
	std::cin >> T;
}

void fillCycle(int i, int number)
{
	if (check[i] != 0)
	{
		return;
	}

	check[i] = number;
	fillCycle(vec[i] - 1, number);
}

void output()
{
	std::cout << ans << '\n';
}

void solve()
{
	while (0 < T)
	{
		int input;
		std::cin >> input;
		vec = std::vector<int>(input);
		check = std::vector<int>(input);
		for (int i = 0; i < input; ++i)
		{
			std::cin >> vec[i];
		}

		int numOfCycles = 0;
		for (int i = 0; i < input; ++i)
		{
			if (check[i] == 0)
			{
				fillCycle(i, ++numOfCycles);
			}
		}
		ans = numOfCycles;
		output();
		--T;
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
	//output();
	return 0;
}