#include <iostream>
using namespace std;

int bucles (int cantidad) {
    int suma = 0;

    for (int i = 1 ; i <= cantidad ; i++)
        suma += i;
    
    return suma;
}

int main () {
    int numero = 10;
    int formula = numero * (numero+1) / 2;

    cout<<"Suma con bucles: "<<bucles(10)<<endl;
    cout<<"Suma con formula: "<<formula<<endl;

    return 0;
}