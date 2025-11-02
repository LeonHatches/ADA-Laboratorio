#include <iostream>
#include <vector>
#include <utility>

using namespace std;

pair <int, vector<int>> backpack (vector<int>& peso, vector<int>& valor, int W) {
    
    return {0, {0}};
}

int main () {
    // DATOS INCIALES
    string objetos[5] = {"Pañuelo", "Diamante", "Dinero", "Collar", "Perfume"};
    vector<int> peso  = {1, 10, 2, 3, 4};
    vector<int> valor = {1, 6, 4, 3, 2};
    int capacidad = 12;

    // MÉTODO
    auto resultado = backpack (peso, valor, capacidad);

    // MOSTRAR OBJETOS
    cout << "Valor Máximo: " << resultado.first << endl;
    cout << "Objetos Seleccionados: ";
    for (int i : resultado.second) {
        cout << objetos[i] << " ";
    }
}