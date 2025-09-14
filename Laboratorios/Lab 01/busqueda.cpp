#include <iostream>
using namespace std;

int algoritmoBusqueda (string clave, string texto) {
    if (texto.length() - clave.length() < 0)
        return -1;

    for (int i = 0 ; i <= texto.length() - clave.length() ; i++) {
        
        if (texto.substr(i, clave.length()) == clave)
            return i;
    }
    
    return -1;
}

int main () {
    string palabra = "final";
    string texto   =
    "Un algoritmo puede dividir un problema grande en partes mas pequenas resolviendo cada parte por separado y luego combinando los resultados este metodo permite reducir la complejidad y encontrar soluciones de manera mas eficiente aplicando la idea de dividir vencer y construir la respuesta paso a paso hasta llegar al resultado final";
    
    int pos = algoritmoBusqueda(palabra, texto);
    
    if (pos == -1)
        cout<<"No se encontró la palabra."<<endl;
    else
        cout<<"La palabra se encuentra en: "<<pos<<endl;   
    
    return 0;
}