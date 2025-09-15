#include <iostream>
#include <vector>
using namespace std;

void printVector(vector <int> &arr) {
    cout << "[" << arr[0];
    for (int i = 1; i < arr.size() - 1; i++) {
        cout << ", " << arr[i];
    }

    cout << ", " << arr[arr.size() - 1] << "]\n";
}


void insertion (vector <int> &arr) {
    
    for (int j, i = 1 ; i < arr.size() ; i++) {
        
        int clave = arr[i];

        for (j = i-1 ; j >= 0 && arr[j] > clave ; j--)
            arr[j+1] = arr[j];
        
        arr[j+1] = clave;
    }
}

int main() {
    vector <int> arr = {5, 2, 9, 1, 6};
    printVector(arr);
    insertion(arr);
    printVector(arr);
}