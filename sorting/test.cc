#include <iostream>

float solve(float a[]) {
    #define min(x, y) (x < y ? x : y)
    float nc = 1 - a[2];
    float nd = 1 - a[3];
    float ans = min(a[0], a[1]);
    ans = min(ans, nc);
    ans = min(ans, nd);
    return ans;
}

int main() {
    float a[] = {1.2, 2.3, 3.4, 4.5};
    std::cout << solve(a) << std::endl;
    return  0;
}