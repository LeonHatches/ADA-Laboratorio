#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

pair<float, vector<float>> backpack (vector<int>& peso, vector<int>& valor, int W) {
    
    int n = peso.size();
    vector <float> fraccion (n, 0.0f);

    vector<int> indices(n);
    for (int i = 0 ; i < n ; i++) indices[i] = i;

    

    return {0, {}};
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
    for (int i = 0 ; i < resultado.second.size() ; i++) {
        if (resultado.second[i] > 0)
            cout << " - " << objetos[i] << " (" << resultado.second[i] * 100 << "% )"<<endl;
    }
}