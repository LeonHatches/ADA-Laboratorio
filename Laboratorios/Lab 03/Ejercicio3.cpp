#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

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

int binarySearch(std::vector<int> &arr, int target) {
    int start = 0, end = arr.size() - 1, med;

    while (start <= end) {
        med = (start + end) / 2;

        if (arr[med] == target)
            return med;
        
        if (arr[med] > target) 
            end = med - 1;
        else 
            start = med + 1;
    }

    return -1;
}

template <typename T>
void mergeSort(std::vector<T> &arr) {
    mergeSort(arr, 0, arr.size() - 1);
}

std::vector<int> generateArray(int n) {
    std::vector<int> arr;
    std::srand(std::time(nullptr));
    for (int i = 0; i < n; i++) {
        arr.push_back(std::rand() % (n + 1));
    }
    return arr;
}

void printVector(std::vector<int> &arr) {
    for (int n : arr)
        std::cout << n << " ";

    std::cout << '\n';
}

int main() {
    std::vector<int> arr = generateArray(50);
    std::cout << "Arreglo Generado\n";
    printVector(arr);
    std::cout << "\n";

    int numeroBuscado = arr[arr.size() / 2];
    std::cout << "Número a buscar: " << numeroBuscado << "\n";
    std::cout << "\n";

    mergeSort(arr);
    std::cout << "Arreglo Ordenado con MergeSort\n";
    printVector(arr);
    std::cout << "\n";

    int numIndex = binarySearch(arr, numeroBuscado);
    std::cout << "Número " << numeroBuscado << " en índice: " << numIndex << "\n";
}