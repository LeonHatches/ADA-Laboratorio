#include <vector>
#include <iostream>
using namespace std;

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

int main () {
    vector <int> arr = {38, 27, 43, 3, 9, 82, 10};

    quickSort(arr, 0, arr.size() - 1);
    for (int i : arr) {
        cout<<i<<" ";
    }

    return 0;
} 