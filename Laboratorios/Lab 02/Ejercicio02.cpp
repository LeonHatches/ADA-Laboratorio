#include <iostream>
#include <utility>
#include <vector>

void printVector(std::vector<float> arr) {
    std::cout << arr[0];

    for (int i = 1; i < arr.size(); i++) {
        std::cout << ", " << arr[i];
    }
    std::cout << "\n";
}

void selectionSort (std::vector<float> &arr) {
    int comparaciones = 0;
    int intercambios = 0;

    for (int i = 0; i < arr.size() - 1; i++) {
        int minIndex = i;
        
        for (int j = i; j < arr.size(); j++) {
            comparaciones++;
            if (arr[minIndex] > arr[j]) {
                minIndex = j;
                intercambios++;
            }
        }
        std::swap(arr[i], arr[minIndex]);
    }

    std::cout << "Comparaciones: " << comparaciones << '\n';
    std::cout << "Intercambios: " << intercambios << '\n';
}

int main() {
    std::vector <float> arr = {1.4, 9.2, 5.2, 8.2, 2.9, 3.1, 10.1, 4.6, 7.8};
    std::cout << "Arreglo original" << '\n';
    printVector(arr);
    std::cout << '\n';
    selectionSort(arr);
    std::cout << "Arreglo ordenado" << '\n';
    printVector(arr);
}