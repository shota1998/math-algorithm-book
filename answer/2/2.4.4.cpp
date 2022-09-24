#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;

ll n, x, a[1000009];

int main() {
  cin >> n >> x;
  for (int i = 0; i < n; i++) cin >> a[i];

  sort(a, a + n);

  ll left = 1, right = n;
  while (left <= right) {
    ll mid = (left + right) / 2;
    if (a[mid] == x) {cout << "Yes: index is " << mid << endl; return 0;}
    if (a[mid] > x) right = mid - 1;
    if (a[mid] < x) left = mid + 1;
  }

  cout << "No" << endl;
  return 0;
}