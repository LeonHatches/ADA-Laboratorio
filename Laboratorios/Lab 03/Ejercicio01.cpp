#include <iostream>
#include <vector>

class Estudiante {
    private:
        std::string codigo;
        std::string nombre;
        float promedioPon;

    public:
        Estudiante() : Estudiante("", "", 0) {}

        Estudiante(std::string codigo, std::string nombre, float promedioPon) {
            this->codigo = codigo;
            this->nombre = nombre;
            this->promedioPon = promedioPon;
        }

        bool operator <(const Estudiante& otro) const {
            return this->nombre < otro.nombre;
        }

        bool operator >(const Estudiante& otro) const {
            return this->nombre > otro.nombre;
        }

        std::string getCodigo() { return codigo; }
        std::string getNombre() { return nombre; }
        float getPromedio() { return promedioPon; }
};

void printListaEstudiantes(std::vector<Estudiante> lista) {
    for (Estudiante estudiante : lista) {
        std::cout << "CODIGO: " << estudiante.getCodigo() 
                  << ", NOMBRE: " << estudiante.getNombre() 
                  << ", PROMEDIO:" << estudiante.getPromedio() << "\n";
    }
}


template <typename T>
void merge(std::vector<T> &arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    std::vector<T> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];

    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
    
    int i = 0, j =0, k = l;

    while (i < n1 && j < n2) {
        if (L[i] < R[j])
            arr[k++] = L[i++];
        else 
            arr[k++] = R[j++];
    }

    while (i < n1)
        arr[k++] = L[i++];
    while (j < n2)
        arr[k++] = R[j++];
}

template <typename T>
void mergeSort(std::vector<T> &arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

template <typename T>
void mergeSort(std::vector<T> &arr) {
    mergeSort(arr, 0, arr.size() - 1);
}


int main() {
    std::vector<Estudiante> lista = {
        Estudiante("E001", "Joaquin Quispe", 15.6),
        Estudiante("E002", "Maria Lopez", 18.2),
        Estudiante("E003", "Carlos Ramirez", 12.9),
        Estudiante("E004", "Ana Torres", 17.5),
        Estudiante("E005", "Luis Fernandez", 14.3),
        Estudiante("E006", "Sofia Castro", 19.0),
        Estudiante("E007", "Diego Morales", 13.7),
        Estudiante("E008", "Camila Rojas", 16.8),
        Estudiante("E009", "Pedro Gonzales", 11.5),
        Estudiante("E010", "Valeria Vargas", 18.9),
        Estudiante("E011", "Ricardo Salazar", 12.2),
        Estudiante("E012", "Fernanda Aguilar", 17.1),
        Estudiante("E013", "Andres Paredes", 15.0),
        Estudiante("E014", "Lucia Mendoza", 19.3),
        Estudiante("E015", "Mateo Delgado", 13.4),
    };

    std::cout << "Lista sin ordenar\n";
    printListaEstudiantes(lista);

    std::cout << "\n";
    mergeSort(lista);

    std::cout << "Lista ordenada\n";
    printListaEstudiantes(lista);
}