#include <iostream>

using namespace std;

int main() {
    int x = 5;
    int y = 10;

    // cout << (x & y) << 1 << endl;

    unsigned a = (x & y) << 1;
    unsigned b = (x & y);
    cout << a << endl;
    cout << (b << 1) << endl;

    return 0;
}
