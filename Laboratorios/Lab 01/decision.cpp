#include <iostream>
using namespace std;

bool palindromo (string str) {
    int size = str.length() / 2;

    for (int i = 0 ; i < size ; i++) {
        if (str[i] != str[str.length() - i])
            return false;
    }

    return true;
}

int main () {
    
    return 0;
}