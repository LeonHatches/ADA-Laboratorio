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

    vector <string> lista1 = {"Daniel", "Carlos", "Beto", "Alfredo"};
    vector <string> lista2 = lista1;

    // Ordenamiento por inserción
    cout<<"El arreglo ordenado (algoritmo) es: "<<endl;
    ordenamiento(lista1);
    
    for (string nombre : lista1) {
        cout<<nombre<<" "<<endl;
    }

    //Biblioteca
    cout<<"El arreglo ordenado (biblioteca) es: "<<endl;
    sort( lista2.begin(), lista2.end() );

    for (string nombre : lista2) {
        cout<<nombre<<" "<<endl;
    }

    return 0;
}