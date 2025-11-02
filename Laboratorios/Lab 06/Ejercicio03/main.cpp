#include <iostream>
#include <vector>
#include <utility>

using namespace std;

pair <int, vector<int>> backpack (vector<int>& peso, vector<int>& valor, int W) {
    
    vector<vector<int>> dp (peso.size() + 1, vector<int>(W + 1, 0));

    // Recorremos objetos
    for (int i = 1 ; i <= peso.size() ; i++) {
        
        // Recorremos todas las capacidades posibles
        for (int j = 0 ; j <= W ; j++) {
            
            // Si el objeto cabe en la mochila
            if (peso[i-1] <= j)
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - peso[i-1]] + valor[i-1]);
            
            // Si no cabe, copio el valor anterior
            else
                dp[i][j] = dp[i-1][j];
        }
    }

    vector<int> objetos;
    int j = W;

    // Se va hacia atrás en la matriz dp
    for (int i = peso.size(); i > 0 ; i--) {
        
        // Si el valor cambia, entonces el obj fue tomado
        if (dp[i][j] != dp[i-1][j]) {
            objetos.push_back(i-1);
            j -= peso[i-1];
        }
    }

    return {dp[peso.size()][W], objetos};
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