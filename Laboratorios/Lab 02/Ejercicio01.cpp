#include <iostream>
#include <vector>
using namespace std;

template <typename T>
void insertion (vector <T>& arr) {
   
    int pasos = 1;
    cout<<"Pasos: "<<ends;

    for (int j, i = 1 ; i < arr.size() ; i++) {
        
        T& clave = arr[i];

        for (j = i-1 ; j >= 0 && arr[j] > clave ; j--) {
            arr[j+1] = arr[j];
            cout<<pasos<<" "<<ends;
            pasos++;
        }
        
        arr[j+1] = clave;
    }
}

int main () {
    
}