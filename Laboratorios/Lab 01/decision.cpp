#include <iostream>
using namespace std;

bool palindromo (string str) {
    int size = str.length() / 2;

    for (int i = 0 ; i < size ; i++) {
        if (str[i] != str[str.length()- 1 - i])
            return false;
    }

    return true;
}

int main () {
    string palabra   = "sometemos";
    string resultado = ( palindromo(palabra) ) ? "SI":"NO";
    
    cout<<"La palabra '"<<palabra<<"' "<<resultado<<" es un palindromo."<<endl;

    return 0;
}