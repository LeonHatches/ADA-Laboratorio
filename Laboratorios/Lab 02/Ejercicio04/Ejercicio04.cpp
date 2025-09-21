#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

struct Juego {
    int id;
    std::string titulo;
    double calificación;

    void mostrarJuego() {
        std::cout << "Id: " << id << ", Titulo: " << titulo << ", Calificacion: " << calificación << '\n';
    }
};

std::vector<Juego> cargarDatos() {
    std::ifstream fich("datos.txt");

    if (!fich.is_open()) {
        std::cout << "Error al abrir ejemplo.dat\n";
        exit(EXIT_FAILURE);
    }

    std::string linea;
    std::vector<Juego> datos;

    while (getline(fich, linea)) {
        std::stringstream ss(linea);

        std::string idStr, tituloStr, calificacionStr;

        getline(ss, idStr, ',');
        getline(ss, tituloStr, ',');
        getline(ss, calificacionStr, ',');

        int id = std::stoi(idStr);
        double calificacion = std::stod(calificacionStr);
        if (tituloStr[0] == ' ') {
            tituloStr.erase(0, 1);
        }

        Juego juego{id, tituloStr, calificacion};

        datos.push_back(juego);
    }

    return datos;
}

void mostrarJuegos(std::vector<Juego> arr) {
    for (Juego juego : arr) {
        juego.mostrarJuego();
    }
}

int main() {
    std::vector<Juego> juegos = cargarDatos();
        mostrarJuegos(juegos);
}