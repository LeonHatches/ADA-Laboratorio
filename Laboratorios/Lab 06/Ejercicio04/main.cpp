#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

pair<float, vector<float>> backpack (vector<int>& peso, vector<int>& valor, int W) {
    
    int n = peso.size();
    vector <float> fraccion (n, 0.0f);

    vector<int> indices(n);
    for (int i = 0 ; i < n ; i++)
        indices[i] = i;

    sort(indices.begin(), indices.end(), [&](int a, int b) {
        return (float) valor[a] / peso[a] > (float) valor[b] / peso[b];
    });

    float valor_max = 0.0f;
    int  pesoActual = 0;

    for (int i : indices) {
        if (pesoActual + peso[i] <= W) {
            
            fraccion[i] = 1.0f;
            pesoActual += peso[i];
            valor_max  += valor[i];
        
        } else {
            
            float restante = W - pesoActual;
            if (restante > 0) {
                fraccion[i] = (float) restante / peso[i];
                valor_max  += valor[i] * fraccion[i];
            }
            break;
        }
    }

    return {valor_max, fraccion};
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
    cout << "Objetos Seleccionados: "<<endl;
    for (int i = 0 ; i < resultado.second.size() ; i++) {
        if (resultado.second[i] > 0)
            cout << " - " << objetos[i] << " ( " << resultado.second[i] * 100 << "% )"<<endl;
    }
}