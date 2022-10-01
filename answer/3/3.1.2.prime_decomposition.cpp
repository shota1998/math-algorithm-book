#include <iostream>
using namespace std;

int main() {
    long long n;
    cin >> n;

    bool flag = false;
    for (long long i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            if (flag == true) cout << " ";
            flag = true;
            n /= i;
            cout << i;
        }
    }
    
    if (n >= 2) {
        if (flag == true) cout << " ";
        flag = true;
        cout << n;
    }

    cout << endl;
    
    return 0;
}