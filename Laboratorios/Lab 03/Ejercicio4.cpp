#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>

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

template<typename T>
int partition(std::vector<T>& arr, int low, int high) {
    T pivot = arr[high];   // pivote
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

template<typename T>
void quickSort(std::vector<T>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

template<typename T>
void quickSort(std::vector<T>& arr) {
    quickSort(arr, 0, arr.size() - 1);
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
    std::vector<int> arr = generateArray(10000);
    std::vector<int> arrCopy = arr;

    auto start1 = std::chrono::high_resolution_clock::now();
    mergeSort(arr);
    auto end1 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration1 = end1 - start1;
    std::cout << "Tiempo de Ejecución (MergeSort): " << duration1.count() << '\n';

    auto start2 = std::chrono::high_resolution_clock::now();
    quickSort(arrCopy);
    auto end2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration2 = end2 - start2;
    std::cout << "Tiempo de Ejecución (QuickSort): " << duration2.count() << '\n';
}