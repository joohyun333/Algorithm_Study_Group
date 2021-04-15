#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <vector>
#include <array>
#include <map>
#include <set>
#include <unordered_map>
#include <cmath>

int N, M, L;
int ans;
std::vector<int> vec;

constexpr int min(int first, int second)
{
	return first < second ? first : second;
}

constexpr int max(int first, int second)
{
	return first < second ? second : first;
}

struct highway
{
	float curr;
	float rests;
	int dist;
};

void input()
{
	std::cin >> N >> M >> L;
	vec.resize(N + 2);
	vec[0] = 0;
	for (int i = 1; i <= N; ++i)
	{
		std::cin >> vec[i];
	}
	vec.back() = L;
	std::sort(vec.begin(), vec.end());
}

void solve()
{
	auto cmp = [](highway& first, highway& second) -> bool {
		return first.curr <= second.curr;
	};
	std::priority_queue<highway, std::vector<highway>, decltype(cmp)> pq(cmp);
	for (int i = 1; i < vec.size(); ++i)
	{
		highway h = { vec[i] - vec[i - 1], 1, vec[i] - vec[i - 1] };
		pq.push(h);
	}

	for (int i = 0; i < M; ++i)
	{
		highway h = pq.top();
		pq.pop();
		h.curr = h.dist / ++h.rests;
		pq.push(h);
	}

	ans = ceilf(pq.top().curr);
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