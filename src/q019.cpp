#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;

ll zeller(ll y, ll m, ll d) {
	if (m < 3) {
		m += 12;
		y--;
	}
	ll h = (d + (13 * (m + 1)) / 5 + y % 100 + (y % 100) / 4 + (y / 100) / 4 - 2 * (y / 100)) % 7;
	h = (h + 7) % 7;

	return (h + 5) % 7 + 1;
}

int main() {
	int t;
	cin >> t;
	while (t--) {
		ll y1, m1, d1, y2, m2, d2;
		scanf("%lld %lld %lld %lld %lld %lld", &y1, &m1, &d1, &y2, &m2, &d2);

		ll cnt = 0;
		for (ll i = y1; i <= y2; i++) {
			for (ll j = 1; j <= 12; j++) {
				if (zeller(i, j, 1) == 7) ++cnt;
			}
		}
		for (ll j = 1; j <= m1; j++)
			if (zeller(y1, j, 1) == 7)
				--cnt;
		if (d1 == 1 && zeller(y1, m1, d1) == 7)
			++cnt;
		for (ll j = m2 + 1; j <= 12; j++)
			if (zeller(y2, j, 1) == 7)
				--cnt;

		printf("%lld\n", cnt);
	}

	return 0;
}
