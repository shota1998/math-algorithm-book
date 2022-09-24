#include <iostream>
#include <string>
#include <sstream>
using namespace std;

typedef long long ll;

ll n;
ll input;
ll answer;

int main () {
  cin >> n;

  for (int i = 0; i < n; i++){
    cin >> input;
    answer += input; 
  }

  cout << answer % 100 << endl;
  return 0;
}