#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void ordenamiento (vector <string> &lista) {
    
    for (int j, i = 1 ; i < lista.size() ; i++) {
        
        string clave = lista[i];

        for (j = i-1 ; j >= 0 && lista[j] > clave ; j--)
            lista[j+1] = lista[j];
        
        lista[j+1] = clave;
    }
}

int main () {
    
    

    return 0;
}