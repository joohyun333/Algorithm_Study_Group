#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>
#include <vector>
#include <array>
#include <bitset>
#include <unordered_map>

int N;
std::vector<std::string> strs;

void input()
{
	std::cin >> N;
	strs = std::vector<std::string>(N);
	for (int i = 0; i < N; ++i)
	{
		std::cin >> strs[i];
	}
}

void solve()
{
	for (auto it : strs)
	{
		std::sort(it.begin(), it.end());
		do
		{
			std::cout << it << '\n';;
		} while (std::next_permutation(it.begin(), it.end()));
	}
}

void output()
{
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