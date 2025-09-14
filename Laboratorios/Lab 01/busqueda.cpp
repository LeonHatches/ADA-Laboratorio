#include <iostream>
using namespace std;

int algoritmoBusqueda (string clave, string texto) {
    if (texto.length() - clave.length() < 0)
        return -1;

    for (int i = 0 ; i < texto.length() - clave.length() ; i++) {
        if (texto.substr(i, i + clave.length()) == clave)
            return i;
    }
    
    return -1;
}

int main () {
    return 0;
}