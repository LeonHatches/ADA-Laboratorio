#include <vector>
#include <iostream>
#include <chrono>
using namespace std;

template <typename T>
int partitionFixed (vector <T>& arr, int low, int high) {
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
void quickSortFixed (vector <T>& arr, int low, int high) {
    if (low < high) {
        int pi = partitionFixed(arr, low, high);
        quickSortFixed (arr, low, pi - 1);
        quickSortFixed (arr, pi + 1, high);
    }
}

template <typename T>
int partitionRandom (vector <T>& arr, int low, int high) {
    
    int random = low + rand() % (high - low + 1);
    swap(arr[random], arr[high]);
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
void quickSortRandom (vector <T>& arr, int low, int high) {
    if (low < high) {
        int pi = partitionRandom (arr, low, high);
        quickSortRandom (arr, low, pi - 1);
        quickSortRandom (arr, pi + 1, high);
    }
}

int main () {
    vector <double> arr1 = {0.97, 0.57, 0.33, 0.31, 0.17, 0.14, 0.12, 0.10, 0.09, 0.01};
    vector <double> arr2 = arr1;

    // Toma de tiempo y método de QUICKSORT FIJO
    auto start1 = chrono::high_resolution_clock::now();
    quickSortFixed(arr1, 0, arr1.size() - 1);
    auto end1 = chrono::high_resolution_clock::now();

    chrono::duration<double> duration1 = end1 - start1;

    cout<<"Arreglo Fijo: ";
    for (double i : arr1) {
        cout<<i<<" ";
    }


    // Toma de tiempo y método de QUICKSORT ALEATORIO
    auto start2 = chrono::high_resolution_clock::now();
    quickSortRandom(arr2, 0, arr2.size() - 1);
    auto end2 = chrono::high_resolution_clock::now();
    
    chrono::duration<double> duration2 = end2 - start2;

    cout<<"\nArreglo Aleatorio: ";
    for (double j : arr2) {
        cout<<j<<" ";
    }

    // Mostrar mensaje
    cout<<"\n| Tiempo de Quicksort (s) | "<<"Fijo: "<<duration1.count()<<" Random: "<<duration2.count()<<endl;
}









