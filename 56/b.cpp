#include <vector>
using namespace std;

void write(int cnt, vector<char>& chars, int& j) {
    if (cnt >= 2) {
        if (cnt < 10) chars[j++] = cnt + '0';
        else if (cnt < 100) 
            { chars[j++] = cnt / 10 + '0'; chars[j++] = cnt % 10 + '0';}
        else if (cnt < 1000) {
            chars[j++] = cnt / 100 + '0'; chars[j++] = (cnt / 10) % 10 + '0';
            chars[j++] = cnt % 10 + '0';
        } else {
            chars[j++] = '1'; chars[j++] = '0'; chars[j++] = '0'; chars[j++] = '0';
        }
    }
}

int compress(vector<char>& chars) {
    int i = 0, j = 0, cnt = 1;
    char c = chars[0];
    for (i = 1;i < chars.size(); i++) {
        if (chars[i] == chars[j]) cnt++;
        else {
            chars[j++] = chars[i];
            write(cnt, chars, j);
            c = chars[i];
            cnt = 1;
        }
    }
    chars[j++] = chars[chars.size() - 1];
    write(cnt, chars, j);
    return j;
}