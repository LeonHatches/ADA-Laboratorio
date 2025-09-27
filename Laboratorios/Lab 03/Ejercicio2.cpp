#include <vector>
#include <iostream>
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