#include <iostream>
#include <vector>
#include <chrono>
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

        // Toma de tiempo y método DE INSERCIÓN
        auto start1 = chrono::high_resolution_clock::now();

        auto end1 = chrono::high_resolution_clock::now();

        chrono::duration<double> duration1 = end1 - start1;

        // Toma de tiempo y método DE SELECCIÓN
        auto start2 = chrono::high_resolution_clock::now();

        auto end2 = chrono::high_resolution_clock::now();

        chrono::duration<double> duration2 = end2 - start2;

        // Mostrar mensaje
        cout<<"| Iteraciones de "<<cantidades[i]<<"| Ins: "<<duration1.count()<<" Sel: "<<duration2.count()<<endl;
    }
}