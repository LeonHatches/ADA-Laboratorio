#include <iostream>
#include <vector>
using namespace std;

template <typename T>
void insertion (vector <T>& arr) {
   
    int pasos = 0;
    cout<<"Pasos: "<<pasos<<" "<<ends;

    for (int j, i = 1 ; i < arr.size() ; i++) {
        
        T clave = arr[i];

        pasos++;
        cout<<pasos<<" "<<ends;

        for (j = i-1 ; j >= 0 && arr[j] > clave ; j--) {
            arr[j+1] = arr[j];
            pasos++;
            cout<<pasos<<" "<<ends;
        }
        
        arr[j+1] = clave;
    }

    cout<<endl;
}

int main () {
    vector <string> orden = {"Alberto", "Banu", "Carlos", "Dante", "Esmeralda", "Fernando"};
    vector <string> reves = {"Fernando", "Esmeralda", "Dante", "Carlos", "Banu", "Alberto"};
    vector <string> aleat = {"Carlos", "Banu", "Alberto", "Esmeralda", "Fernando", "Dante"};

    // LISTA ORDENADA
    insertion(orden);
    cout<<"Lista ordenada: "<<ends;
    
    for (string nombre : orden)
        cout<<nombre<<" "<<ends;
    
    cout<<endl;
    

    // LISTA AL REVÉS
    insertion(reves);
    cout<<"Lista al revés: "<<ends;
    
    for (string nombre : reves)
        cout<<nombre<<" "<<ends;
    
    cout<<endl;

    // LISTA ALEATORIA
    insertion(aleat);
    cout<<"Lista aleatoria: "<<ends;
    
    for (string nombre : aleat)
        cout<<nombre<<" "<<ends;
    
    cout<<endl;
}