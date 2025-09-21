#include <iostream>
#include <vector>
using namespace std;

template <typename T>
void insertion (vector <T>& arr) {
   
    int pasos = 0;
    cout<<"Pasos: "<<pasos<<" "<<ends;

    for (int j, i = 1 ; i < arr.size() ; i++) {
        
        T& clave = arr[i];

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

    insertion(orden);
    cout<<"Lista ordenada: "<<ends;
    
    for (string nombre : orden)
        cout<<nombre<<" "<<ends;
    
    cout<<endl;
    
}