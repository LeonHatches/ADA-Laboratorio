#include <iostream>
using namespace std;

int algoritmoBucle (int numero1, int numero2) {
    
    int mcd = 1;
    for (int i = 1; i < numero2/2; i++)
    {
        if (numero1 % i == 0 && numero2 % i == 0)
            mcd *= i;
    }
    
    return mcd;
}

int algoritmoEuclides (int numero1, int numero2) {

    // Excepciones
    if (numero1 == 0 && numero2 == 0)
        return -1;

    if (numero2 == 0)
        return numero1;

    int residuo;    
    do {
        residuo = numero1 % numero2;
        numero1 = numero2;
        numero2 = residuo;

    } while (numero2 != 0);
    
    return abs(numero1);
}

int main () {
    const int NUMERO1 = 32, NUMERO2 = 8;
    int resultadoBucles, resultadoEuclides;

    resultadoBucles   = algoritmoBucle(NUMERO1, NUMERO2);
    resultadoEuclides = algoritmoEuclides(NUMERO1, NUMERO2);

    cout << "Resultado para A. Euclides: " << resultadoEuclides << endl;
    cout << "Resultado para A. con bucles: " << resultadoBucles << endl;

    return 0;
}