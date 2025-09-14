#include <iostream>
using namespace std;

int algoritmoBucle (int numero1, int numero2) {
    
    numero1 = abs(numero1);
    numero2 = abs(numero2);

    if (numero1 == 0 && numero2 == 0)
        return 0;

    if (numero1 == 0 || numero2 == 0)
        return numero1 + numero2;

    int menor = (numero1 < numero2) ? numero1 : numero2;
    for (int i = menor; i > 0; i--)
    {
        if (numero1 % i == 0 && numero2 % i == 0)
            return i;
    }
}

int algoritmoEuclides (int numero1, int numero2) {

    // Excepciones
    if (numero1 == 0 && numero2 == 0)
        return 0;

    if (numero1 == 0 || numero2 == 0)
        return abs(numero1 + numero2);

    int residuo;    
    do {
        residuo = numero1 % numero2;
        numero1 = numero2;
        numero2 = residuo;

    } while (numero2 != 0);
    
    return abs(numero1);
}

int main () {
    const int NUMERO1 = 0, NUMERO2 = 0;
    int resultadoBucles, resultadoEuclides;

    resultadoBucles   = algoritmoBucle(NUMERO1, NUMERO2);
    resultadoEuclides = algoritmoEuclides(NUMERO1, NUMERO2);
    cout << "Resultado para A. Euclides: " << resultadoEuclides << endl;
    cout << "Resultado para A. con bucles: " << resultadoBucles << endl;

    return 0;
}