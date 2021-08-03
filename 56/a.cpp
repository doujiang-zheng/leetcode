# include <iostream>
#include <vector>
using namespace std;

bool isOneBitCharacter(vector<int>& bits) {
    int i;
    for (i = 0; i < bits.size();) {
        if (bits[i] == 0) i++;
        else i += 2;
    }
    if (i == bits.size()) return true;
    else return false;
}

int main() {
    std::cout << "hello, world!" << std::endl;
    return 0;
}