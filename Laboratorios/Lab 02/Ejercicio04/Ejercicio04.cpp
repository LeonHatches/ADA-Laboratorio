#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <chrono>

class Juego {
    private:
        int id;
        std::string titulo;
        double calificacion;

    public:
        Juego(int id, std::string titulo, double calificacion) {
            this->id = id;
            this->calificacion = calificacion;
            this->titulo = titulo;
        }

        bool operator >(const Juego& juego) {
            return (this-> calificacion > juego.calificacion);
        }

        bool operator <(const Juego& juego) {
            return (this-> calificacion < juego.calificacion);
        }

        int getId() { return id; }
        std::string getTitulo() { return titulo; }
        double getCalificacion() { return calificacion; }
};


template <typename T>
void insertionSort (std::vector <T>& arr) {
    int comparaciones = 0;
    int intercambios = 0;

    for (int j, i = 1 ; i < arr.size() ; i++) {
        
        T clave = arr[i];

        for (j = i-1 ; j >= 0; j--) {
            comparaciones++;
            if (arr[j] < clave) {
                arr[j+1] = arr[j];
                intercambios++;
            } else {
                break;
            }
        }
        
        arr[j+1] = clave;
    }

    std::cout << "Comparaciones = " << comparaciones << "\tIntercambios = " << intercambios << '\n';
}

template <typename T>
void selectionSort (std::vector <T>& arr) {
    int comparaciones = 0;
    int intercambios = 0;

    for (int max, i = 0 ; i < arr.size()-1 ; i++) {

        max = i;
        for (int j = max+1 ; j < arr.size() ; j++) {
            comparaciones++;

            if (arr[j] > arr[max]) {
                max = j;
            }
        }
        intercambios++;
        std::swap(arr[i], arr[max]);
    }

    std::cout << "Comparaciones = " << comparaciones << "\tIntercambios = " << intercambios << '\n';
}

Juego getGameFromLine(std::string linea) {
    std::stringstream ss(linea);

    std::string idStr, tituloStr, calificacionStr;

    getline(ss, idStr, ',');
    getline(ss, tituloStr, ',');
    getline(ss, calificacionStr, ',');

    if (tituloStr[0] == ' ') {
        tituloStr.erase(0, 1);
    }

    if (calificacionStr[0] == ' ') {
        calificacionStr.erase(0, 1);
    }

    int id = std::stoi(idStr);
    double calificacion = std::stod(calificacionStr);

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
        salida << juego.getId() << ',' << juego.getTitulo() << ',' << juego.getCalificacion() << '\n';
    }
}

int main() {
    std::vector<Juego> juegos = cargarDatos();
    std::vector<Juego> copia = juegos;


    // Ordernar con InsertionSort
    std::cout << "Ordenando arreglo con InsertionSort\n";
    auto start1 = std::chrono::high_resolution_clock::now();
    insertionSort(juegos);
    auto end1 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration1 = end1 - start1;
    std::cout << "Tiempo de Ejecución: " << duration1.count() << '\n';

    guardarJuegos(juegos, "insertionSort.csv");

    std::cout << '\n';

    // Ordernar con SelectionSort
    std::cout << "Ordenando arreglo con SelectionSort\n";
    auto start2 = std::chrono::high_resolution_clock::now();
    selectionSort(copia);
    auto end2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration2 = end2 - start2;
    std::cout << "Tiempo de Ejecución: " << duration2.count() << '\n';

    guardarJuegos(copia, "selectionSort.csv");
}