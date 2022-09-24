#include <iostream>
using namespace std;
typedef long long ll;

int main() {
  ll a, b, c, count = 1;
  cin >> a >> b;

  while (true) {
    if (a == b) {
      break;
    } else if (a > b) {
      a /= 2;
    } else {
      a += (a/2); 
      int c = a; 
    }

    count++;
  }

  cout << count << endl;
  return 0;
}