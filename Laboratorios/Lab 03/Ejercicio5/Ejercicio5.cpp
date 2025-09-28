#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <chrono>
using namespace std;


class Producto {
    private:
        int id;
        string nombre;
        double precio;

    public:
        Producto (int id, string nombre, double precio) {
            this->id = id;
            this->nombre = nombre;
            this->precio = precio;
        }

        bool operator >(const Producto& producto) {
            return (this->precio > producto.precio);
        }

        bool operator <(const Producto& producto) {
            return (this->precio < producto.precio);
        }

        int getId () { return id; }
        string getNombre () { return nombre; }
        double getPrecio () { return precio; }

        string toStr() const {
            return "| "+to_string(id)+", "+nombre+", "+to_string(precio)+" |";
        }
};


//---------------------- MERGESORT ---------------------- 

template <typename T>
void merge(vector<T> &arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    vector<T> L(n1), R(n2);

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
void mergeSort(vector<T> &arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

template <typename T>
void mergeSort(vector<T> &arr) {
    mergeSort(arr, 0, arr.size() - 1);
}


// -------------------- QUICKSORT -----------------------

template <typename T>
int partition(vector <T>& arr, int low, int high) {
    T pivot = arr[high];
    int i = low - 1;

    for (int j = low ; j <= high - 1 ; j++) {
        
        if (arr[j] < pivot)
            swap(arr[++i], arr[j]);
    }

    swap(arr[i+1], arr[high]);
    return i+1;
}

template <typename T>
void quickSort (vector <T>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

template <typename T>
void quickSort (vector <T>& arr) {
    quickSort (arr, 0, arr.size() - 1);
}

// -----------------------------------------------------------


Producto getProductoFromLine (string linea) {
    stringstream ss(linea);

    string idStr, nombreStr, precioStr;

    getline(ss, idStr, ',');
    getline(ss, nombreStr, ',');
    getline(ss, precioStr, ',');
    
    if (nombreStr[0] == ' ') {
        nombreStr.erase(0, 1);
    }

    if (precioStr[0] == ' ') {
        precioStr.erase(0, 1);
    }

    int id = stoi(idStr);
    double precio = stod(precioStr);

    return {id, nombreStr, precio};
}


vector <Producto> cargarDatos () {
    
    ifstream fich("datos.txt");

    if(!fich.is_open()) {
        cout<<"Error al abrir los archivos."<<endl;
        exit(EXIT_FAILURE);
    }

    string linea;
    vector <Producto> datos;

    while (getline(fich, linea))
        datos.push_back(getProductoFromLine(linea));
    
    return datos;
} 


