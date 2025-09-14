#include <iostream>
using namespace std;

int algoritmoBucle (int numero1, int numero2) {
    return 0;
}

int algoritmoEuclides (int numero1, int numero2) {
    int residuo;

    do {
        residuo = numero1 % numero2;
        numero1 = numero2;
        numero2 = residuo;

    } while (numero2 != 0);
    
    return numero1;
}

int main () {
    const int NUMERO1 = 12, NUMERO2 = 21;
    int resultadoBucles, resultadoEuclides;

    resultadoBucles   = algoritmoBucle(NUMERO1, NUMERO2);
    resultadoEuclides = algoritmoEuclides(NUMERO1, NUMERO2);

    cout << "Resultado para A. Euclides: " << resultadoEuclides << endl;
    cout << "Resultado para A. con bucles: " << resultadoBucles << endl;

    return 0;
}