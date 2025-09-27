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

template <typename T>
int partitionRandom (vector <T>& arr, int low, int high) {
    
    int random = low + rand() % (high - low - 1);
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










