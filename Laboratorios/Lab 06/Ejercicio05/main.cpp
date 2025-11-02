#include <iostream>
#include <vector>

int calcularFormas(int n) {
    if (n < 0) {
        std::cout << "Error: entrada negativa\n";
        return -1;
    }

    if (n <= 2)
        return n;

    auto pasosPorEscalon = std::vector<int>(n + 1);

    pasosPorEscalon[0] = 1;
    pasosPorEscalon[1] = 1;
    pasosPorEscalon[2] = 2;

    for (int i = 3; i <= n; i++) {
        pasosPorEscalon[i] = pasosPorEscalon[i - 1] + pasosPorEscalon[i - 2] + pasosPorEscalon[i - 3];
    }

    return pasosPorEscalon[n];
}

int main() {
    std::cout << "Calcular formas de llegar por escalon\n";
    std::cout << "Solo se puede pasar de 1, 2 o 3 escalones por paso\n";

    std::cout << "\nFormas de llegar a Escalon (N):\n";

    for (int i = 1; i <= 30; i++) {
        std::cout << "Escalon(" << i << ") = " << calcularFormas(i) << "\n";
    }
}
