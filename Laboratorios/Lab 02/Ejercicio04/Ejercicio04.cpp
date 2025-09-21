#include <iostream>
#include <vector>
#include <fstream>

std::vector<std::string> cargarDatos() {
    std::ifstream fich("datos.txt");

    if (!fich.is_open()) {
        std::cout << "Error al abrir ejemplo.dat\n";
        exit(EXIT_FAILURE);
    }

    std::string linea;
    std::vector<std::string> datos;

    while (getline(fich, linea)) {
        datos.push_back(linea);
    }

    return datos;
}

void printVector(std::vector<std::string> arr) {
    for (std::string juego : arr) {
        std::cout << juego << '\n';
    }
}

int main() {
    std::vector<std::string> juegos = cargarDatos();
    printVector(juegos);
}