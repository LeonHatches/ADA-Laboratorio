#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

struct Juego {
    int id;
    std::string titulo;
    double calificacion;

    bool operator > (const Juego& juego) {
        return (this-> calificacion > juego.calificacion);
    }

    bool operator < (const Juego& juego) {
        return (this-> calificacion < juego.calificacion);
    }
};

template <typename T>
void insertionSort (std::vector <T>& arr) {
    for (int j, i = 1 ; i < arr.size() ; i++) {
        
        T clave = arr[i];

        for (j = i-1 ; j >= 0 && arr[j] < clave ; j--) {
            arr[j+1] = arr[j];
        }
        
        arr[j+1] = clave;
    }
}

template <typename T>
void selectionSort (std::vector <T>& arr) {
    for (int max, i = 0 ; i < arr.size()-1 ; i++) {

        max = i;
        for (int j = max+1 ; j < arr.size() ; j++) {
            
            if (arr[j] > arr[max])
                max = j;
        }
        std::swap(arr[i], arr[max]);
    }
}

Juego getGameFromLine(std::string linea) {
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

    return {id, tituloStr, calificacion};
}

std::vector<Juego> cargarDatos() {
    std::ifstream fich("datos.txt");

    if (!fich.is_open()) {
        std::cout << "Error al abrir ejemplo.dat\n";
        exit(EXIT_FAILURE);
    }

    std::string linea;
    std::vector<Juego> datos;

    while (getline(fich, linea)) {
        datos.push_back(getGameFromLine(linea));
    }

    return datos;
}

void guardarJuegos(std::vector<Juego> juegos, std::string nombreArchivo) {
    std::ofstream salida(nombreArchivo);

    salida << "id,título,calificacion\n";

    for (Juego juego : juegos) {
        salida << juego.id << ',' << juego.titulo << ',' << juego.calificacion << '\n';
    }
}

int main() {
    std::vector<Juego> juegos = cargarDatos();
    std::vector<Juego> copia = juegos;

    // Ordernar con InsertionSort
    insertionSort(juegos);
    guardarJuegos(juegos, "insertionSort.csv");

    // Ordernar con SelectionSort
    selectionSort(copia);
    guardarJuegos(copia, "selectionSort.csv");
}