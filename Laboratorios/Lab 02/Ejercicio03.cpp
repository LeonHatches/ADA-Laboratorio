#include <iostream>
#include <vector>
using namespace std;

template <typename T>
void insertion (vector <T>& arr) {

    for (int j, i = 1 ; i < arr.size() ; i++) {
        
        T clave = arr[i];

        for (j = i-1 ; j >= 0 && arr[j] > clave ; j--)
            arr[j+1] = arr[j];

        arr[j+1] = clave;
    }
}

int main () {
    vector <int> cantidades = {1000, 5000, 10000};
    
    for (int i = 0 ; i < cantidades.size() ; i++) {

        // Se crea los vectores de 1k, 5k y 10k
        vector <int> list1 (cantidades[i], 0);
        for (int n = 0, i = list1.size() ; i > 0 ; i--)
            { list1[n] = i; n++; }
        
        vector <int> list2 = list1;


    }
}